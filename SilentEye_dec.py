import sys
from PIL import Image
import cast_function as cs


def jump_num_iterations(matrix):
    my_temp = ""
    num_of_iterations = ""
    num_of_jump = ""
    count = 0
    j = 0
    i = 0
    flag = 0
    while my_temp != "$":
        if count <= 8:
            my_temp += str(cs.integer_to_binary(matrix[i][j])[7])
            count += 1
        if count == 8:
            my_temp = str(cs.binary_to_ascii(my_temp))

            if my_temp != "$":
                if flag == 1:
                    num_of_iterations += my_temp
                if my_temp == '^':
                    flag = 1
                if flag == 1:
                    i += int(num_of_jump)
                if flag == 0:
                    num_of_jump += my_temp
                my_temp = ""
                j += 1
            count = 0
        j += 1
        if j >= 3:
            i += 1
            j = 0
    temp = (num_of_jump, num_of_iterations)
    return temp


def SilentEye_decoding(matrix):
    my_tuple = jump_num_iterations(matrix)
    jump = int(my_tuple[0])
    end = my_tuple[1]
    start = (len(my_tuple[0])*3)+3+jump
    counter = 0
    word = 0
    my_str = ""
    decoded_word = ""

    for pixel in matrix:
        if counter != start:
            counter += 1
        else:
            for pixel_cell in pixel:

                if word == 8:
                    decoded_word += str(cs.binary_to_ascii(my_str))
                    word = 0
                    my_str = ""
                    counter = 0
                    start = jump
                    break

                my_str += str(cs.integer_to_binary(pixel_cell)[7])
                word += 1
        if len(decoded_word) == int(end)+1+len(end):
            break

    return decoded_word[1+len(end):]


def main(image_path):

    im = Image.open(image_path)
    m = im.getdata()
    print(SilentEye_decoding(m))


main(sys.argv[1])
