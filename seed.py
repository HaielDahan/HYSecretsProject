from PIL import Image
from PIL.PngImagePlugin import PngInfo
import aes_seed
def set_meta(path,seed):
    targetImage = Image.open(path)
    metadata = PngInfo()
    metadata.add_text("Number" , str(seed))
    targetImage.save(path[:-4]+"_seed.png", pnginfo=metadata)
    return seed

def set_sec_meta(path,seed):
    targetImage = Image.open(path)
    metadata = PngInfo()

    seed_aes_val = aes_seed.aes_encrypt(str(seed))
    print(seed_aes_val)
    print(type(seed_aes_val))
    metadata.add_text("Number" , seed_aes_val)

    try:
        new_string = path.rsplit("\\", 1)[0]
        print("new:", new_string)
        image_name = path.split('\\')
        print("im name 1 :", image_name)
        image_name = image_name[-1].split('.')[0]
        print("im name 2 :", image_name)
        new_path = new_string + "\\testFolder\\"+image_name[:-5]+"_HYS.png"
        targetImage.save(new_path, pnginfo=metadata)
    except:
        new_string = path.rsplit("/", 1)[0]
        print("new:", new_string)
        image_name = path.split('/')
        print("im name 1 :", image_name)
        image_name = image_name[-1].split('.')[0]
        print("im name 2 :", image_name)
        new_path = new_string + "/testFolder/" + image_name[:-5] + "_HYS.png"
        targetImage.save(new_path, pnginfo=metadata)

    im = Image.open(new_path)
    return im

   # לבדוק למה זה לא עובד
    # print("---targetImage: ", targetImage)
    # print("target number :", targetImage.text.get('Number'))
    # print("target number :", im.text.get('Number'))