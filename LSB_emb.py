from PIL import Image
import cast_function as cs
import sys
import file_reader as fr

def lsb_embedding(im, my_str):
    x = len(my_str)
    my_str = str(x) + "$" + my_str
    my_matrix_image = im.getdata()  # pixels matrix.

    my_char_place = 0  # the current index of my_str
    my_char = my_str[my_char_place]  # the current char of my str the loop hides it now.
    my_bin = cs.char_to_binary(my_char)  # the current char in binary 8 bits
    my_point = 0  # the current index of my bin in hiding loop.

    flag = 0  # flag = 0 - still hiding, flag = 1 - regular copy
    new_matrix = []
    j = -1

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
        new_matrix[j] = tuple(new_matrix[j])

    new_im = Image.new(im.mode, im.size)
    new_im.putdata(new_matrix)

    return new_im


def main(path, my_str):
    # new_image_path = "\\testFolder\\"+image_path.rsplit('.', 1)[0]+'_LSBE.png'
    im = Image.open(path)

    try:
        new_string = path.rsplit("\\", 1)[0]
        print("new:", new_string)
        image_name = path.split('\\')
        print("im name 1 :", image_name)
        image_name = image_name[-1].split('.')[0]
        print("im name 2 :", image_name)
        new_path = new_string + "\\testFolder\\" + image_name + "_LSBE.png"
        # my_str = fr.file_read("text.txt")
        lsb_embedding(im, my_str).save(new_path)
        # print("done!\nFile Location: "+new_image_path)
    except:
        new_string = path.rsplit("/", 1)[0]
        print("new:", new_string)
        image_name = path.split('/')
        print("im name 1 :", image_name)
        image_name = image_name[-1].split('.')[0]
        print("im name 2 :", image_name)
        new_path = new_string + "/testFolder/" + image_name + "_LSBE.png"
        # my_str = fr.file_read("text.txt")
        lsb_embedding(im, my_str).save(new_path)
        # print("done!\nFile Location: "+new_image_path)



# main(sys.argv[1])
