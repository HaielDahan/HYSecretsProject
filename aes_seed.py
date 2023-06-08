from Cryptodome.Cipher import AES
# from Cryptodome.PublicKey import RSA
# from Cryptodome import Random

def aes_encrypt(str_to_en):

    # RSA Method for later do not delete it

    # e = 54729
    # private_key = RSA.generate(1024, Random.new().read, e)  # generate public and private keys
    # pv_key = str(private_key)[19:]
    # pv_key = bytes(pv_key, 'utf-8')

    # pv key aes:
    pv_key = bytes("3147320548027161",'utf-8')

    # cipher and nonce init
    cipher = AES.new(pv_key, AES.MODE_EAX, nonce = b'2\x07-\x91v\xbf\x00\x99k\xc7\x96\x9f\xafeF@')

    str_to_en = bytes(str_to_en, 'utf-8')
    str_to_en = cipher.encrypt(str_to_en)

    string_data = str_to_en.decode('utf-8')

    return string_data


def aes_decrypt(str_to_dec):

    str_to_dec = str_to_dec.encode('utf-8')
    cipher = AES.new(bytes("3147320548027161",'utf-8'), AES.MODE_EAX, nonce = b'2\x07-\x91v\xbf\x00\x99k\xc7\x96\x9f\xafeF@')
    return cipher.decrypt(str_to_dec).decode('utf-8')