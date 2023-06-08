from PIL import Image
import os
import cast_function as cs
import seed
import random_seed as rs
import sys
import file_reader as fr



def HYS_encoding(image_path, message):
    # insert metadata to the image
    seed_val = seed.set_meta(image_path,rs.get_random_seed())


    new_image_path = image_path[:-4]+"_seed.png"
    im = Image.open(new_image_path)
    pixel_amount = im.size[0]*im.size[1]

    jump_list = rs.generate_random_list(int(im.text.get('Number')),pixel_amount)


    list = [0] * pixel_amount

    i=0
    pixel_summer=0

    while i<len(jump_list)-1:
        index_value = jump_list[i]
        pixel_summer = pixel_summer + index_value
        list[pixel_summer] = 1
        i +=1

    count = list.count(1)
    #print("count = " + str(count))
    number_of_chars = (count * 3 // 8) - 3
    # print(number_of_chars)

    #print("Text len you can hide: " + str(number_of_chars))
    new_image_path = image_path
    im = Image.open(new_image_path)
    my_matrix_image = im.getdata()
    # my_str = fr.file_read("text.txt")
    my_str = message

    if len(my_str)>number_of_chars:
        my_str = my_str[:my_str-number_of_chars]
    #my_str = "Hello Haiel How are you?"

    my_str += "$^$"

    # print("my str len:" + str(len(my_str)))

    my_char_place = 0  # the current index of my_str
    my_char = my_str[my_char_place]  # the current char of my str the loop hides it now.
    my_bin = cs.char_to_binary(my_char)  # the current char in binary 8 bits
    my_point = 0  # the current index of my bin in hiding loop.

    flag = 0  # flag = 0 - still hiding, flag = 1 - regular copy
    new_matrix = []
    j = -1

    index = 0

    for pixel in my_matrix_image:

        if my_point == 8:
            my_char_place += 1
            if my_char_place >= len(my_str):
                flag = 1

            if flag == 0:
                my_char = my_str[my_char_place]
                my_bin = cs.char_to_binary(my_char)
                my_point = 0

        new_matrix.append([])
        j += 1
        if list[index] == 1:
            for i in pixel:
                bin_i = cs.integer_to_binary(i)

                if flag == 0:
                    if my_bin[my_point] != bin_i[7]:
                        bin_i = bin_i[:7] + my_bin[my_point]
                        new_matrix[j].append(int(bin_i, 2))
                    else:
                        new_matrix[j].append(int(bin_i, 2))
                    my_point += 1
                else:
                    new_matrix[j].append(int(bin_i, 2))

                if my_point == 8:
                    my_char_place += 1
                    if my_char_place < len(my_str):
                        my_char = my_str[my_char_place]
                        my_bin = cs.char_to_binary(my_char)
                        my_point = 0
                    else:
                        flag = 1
        else:
            new_matrix[j] = pixel

        index += 1
        new_matrix[j] = tuple(new_matrix[j])

    new_im = Image.new(im.mode, im.size)
    new_im.putdata(new_matrix)
    new_im.save(new_image_path[:-4] + "_temp.png")

    im = seed.set_sec_meta(new_image_path[:-4] + "_temp.png",seed_val)

    try:

        os.remove(new_image_path[:-4]+"_seed.png")
        os.remove(new_image_path[:-4] + "_temp.png")
    except:
        pass
    return im
# def main(image_path):
#
#     HYS_encoding(image_path)
#
# main(sys.argv[1])

