import cast_function as cs
from PIL import Image
import sys
import file_reader as fr

def SilentEye_embedding(im, my_str, jump):
    x = len(my_str)
    my_str = str(jump) + "^" + str(x) + "$" + my_str
    my_matrix = im.getdata()
    eight_counter = 0
    flag = 0
    jump_flag = 0

    my_char_place = 0   # the current index of my_str
    my_char = my_str[my_char_place]     # the current char of my str the loop hides it now.
    my_bin = cs.char_to_binary(my_char)    # the current char in binary 8 bits
    my_point = 0    # the current index of my bin in hiding loop.
    new_matrix = []

    j = -1

    for pixel in my_matrix:

        if jump_flag == 0:
            j += 1
            new_matrix.append([])
            for i in pixel:
                bin_i = cs.integer_to_binary(i)
                if my_point != 8:
                    if my_bin[my_point] != bin_i[7]:
                        bin_i = bin_i[:7] + my_bin[my_point]
                        new_matrix[j].append(int(bin_i, 2))
                    else:
                        new_matrix[j].append(int(bin_i, 2))

                    my_point += 1

                else:
                    if my_char == '^' and my_point == 8:
                        jump_flag = 1
                        new_matrix[j].append(int(bin_i, 2))
                        my_char_place += 1
                        my_char = my_str[my_char_place]
                        my_bin = cs.char_to_binary(my_char)
                        my_point = 0
                        flag = 1
                        break

                    my_char_place += 1
                    my_char = my_str[my_char_place]
                    my_bin = cs.char_to_binary(my_char)
                    my_point = 0
                    new_matrix[j].append(int(bin_i, 2))

            new_matrix[j] = tuple(new_matrix[j])

        else:
            if flag == 0:
                if eight_counter < 8:
                    new_matrix.append([])
                    j += 1

                    for i in pixel:
                        bin_i = cs.integer_to_binary(i)
                        if my_point < 8 and my_char_place < len(my_str):
                            if my_bin[my_point] != bin_i[7]:
                                bin_i = bin_i[:7] + my_bin[my_point]
                                new_matrix[j].append(int(bin_i, 2))
                            else:
                                new_matrix[j].append(int(bin_i, 2))
                            my_point += 1
                        else:
                            new_matrix[j].append(int(bin_i, 2))
                            my_point = 0
                            my_char_place += 1
                            if my_char_place < len(my_str):
                                my_char = my_str[my_char_place]
                                my_bin = cs.char_to_binary(my_char)

                        eight_counter += 1
                        if eight_counter > 8:
                            eight_counter = 0
                            flag = 1
            else:

                eight_counter += 1
                x = list(pixel)
                new_matrix.append(x)
                j += 1

                if eight_counter == jump:
                    eight_counter = 0
                    flag = 0
        new_matrix[j] = tuple(new_matrix[j])

    new_im = Image.new(im.mode, im.size)
    new_im.putdata(new_matrix)
    return new_im


def main(path,my_str, jump):

    im = Image.open(path)

    try:
        new_string = path.rsplit("\\", 1)[0]
        #print("new:", new_string)
        image_name = path.split('\\')
        #print("im name 1 :", image_name)
        image_name = image_name[-1].split('.')[0]
        #print("im name 2 :", image_name)
        new_path = new_string + "\\testFolder\\" + image_name + "_SE.png"

        #new_image_path = image_path.rsplit('.', 1)[0]+"\\testFolder\\"+ '_SE.png'
        # jump = int(input("Enter your jump rate:"))
        # my_str = fr.file_read("text.txt")
        SilentEye_embedding(im, my_str, jump).save(new_path)
        # print("done!\nFile Location: "+new_image_path)
    except:
        new_string = path.rsplit("/", 1)[0]
        #print("new:", new_string)
        image_name = path.split('/')
        #print("im name 1 :", image_name)
        image_name = image_name[-1].split('.')[0]
        #print("im name 2 :", image_name)
        new_path = new_string + "/testFolder/" + image_name + "_SE.png"

        # new_image_path = image_path.rsplit('.', 1)[0]+"\\testFolder\\"+ '_SE.png'
        # jump = int(input("Enter your jump rate:"))
        # my_str = fr.file_read("text.txt")
        SilentEye_embedding(im, my_str, jump).save(new_path)
        # print("done!\nFile Location: "+new_image_path)



# main(sys.argv[1])
