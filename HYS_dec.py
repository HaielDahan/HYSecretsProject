from PIL import Image
import random_seed as rs
import cast_function as cs
import sys
import aes_seed


def dec_HYS(path):
    im = Image.open(path)
    try:
        seed_val = im.text.get('Number')
        # print(seed_val)
        seed_val = int(aes_seed.aes_decrypt(seed_val))
        # print(seed_val)
        # print(type(seed_val))
    except:
        return (im, "error")
    pixel_amount = im.size[0] * im.size[1]
    jump_list = rs.generate_random_list(seed_val,pixel_amount)

    list = [0] * pixel_amount

    i=0
    pixel_summer=0

    while i < len(jump_list)-1:
        index_value = jump_list[i]
        pixel_summer = pixel_summer + index_value
        list[pixel_summer] = 1
        i += 1

    matrix = im.getdata()

    word = 0
    my_str = ""
    decoded_word = ""

    index_list = 0

    for pixel in matrix:
        if list[index_list] == 1:
            for RGB in pixel:

                if word == 8:
                    decoded_word += str(cs.binary_to_ascii(my_str))
                    word = 0
                    my_str = ""

                my_str += str(cs.integer_to_binary(RGB)[7])
                word += 1
        index_list+=1


        if decoded_word[-3::] == "$^$":
            decoded_word = decoded_word[:-3]
            break

    # print(decoded_word)
    return (im,decoded_word)


# def main(path):
#     print(dec_HYS(path))
#
#
# main(sys.argv[1])