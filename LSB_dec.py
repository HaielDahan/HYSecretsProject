import sys
from PIL import Image
import cast_function as cs


def number_of_iterations(matrix):
    my_temp = ""
    num_of_iterations = ""
    count = 0
    j = 0
    i = 0
    while my_temp != "$":
        if count <= 8:
            my_temp += str(cs.integer_to_binary(matrix[i][j])[7])
            count += 1
        if count == 8:
            my_temp = str(cs.binary_to_ascii(my_temp))
            if my_temp != "$":
                num_of_iterations += my_temp
                my_temp = ""
            count = 0
        j += 1
        if j >= 3:
            i += 1
            j = 0

    return num_of_iterations


def lsb_decoding(matrix):
    start = (len(number_of_iterations(matrix)) + 1) * 8
    end = int(number_of_iterations(matrix))
    counter = 0
    word = 0
    my_str = ""
    decoded_word = ""
    for i in matrix:
        for j in i:
            if counter == start:
                if word == 8:
                    decoded_word += str(cs.binary_to_ascii(my_str))
                    word = 0
                    my_str = ""

                my_str += str(cs.integer_to_binary(j)[7])
                word += 1

            else:
                counter += 1

        if len(decoded_word) == end:
            break
    return decoded_word


def main(image_path):

    im = Image.open(image_path)
    m = im.getdata()
    print(lsb_decoding(m))


main(sys.argv[1])
