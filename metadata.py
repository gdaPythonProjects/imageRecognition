from PIL import Image
from PIL.ExifTags import TAGS

def getTag(img):
    ret = {}
    image = Image.open(str(img))
    info = image._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
        print(ret)
    return ret