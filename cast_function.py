def char_to_binary(c):
    byte_array = c.encode('utf-8')
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = str(bin(binary_int))
    binary_string = str(binary_string[0]) + str(binary_string[2:])
    while len(binary_string) < 8:
        binary_string = '0' + binary_string
    return binary_string


def integer_to_binary(integer):
    my_str = format(integer, 'b')
    while len(my_str) < 8:
        my_str = '0' + my_str
    return str(my_str)


def binary_to_ascii(my_str):
    my_str = int(my_str, 2)
    my_str = chr(my_str)
    return my_str
