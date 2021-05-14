import urllib.request
from PIL import Image
import const_reader
import image_maker

URL = "https://raw.githubusercontent.com/wemos/LOLIN_EPD_Library/master/examples/test_2_13_inch_212x104_TRI-COLOR/image.h"


if __name__ == "__main__":
    wid = 212
    hgt = 104
    BL=(0,0,0)
    RB=(255,0,0)
    im=Image.new('RGB', (wid, hgt), color=(255,255,255,0))
    try:
        with urllib.request.urlopen(URL) as f:
            contents = f.read().decode('utf-8')
            img_data = const_reader.read_consts(contents)
    except urllib.error.URLError as e:
        print(e.reason)
    image_maker.run(img_data['gImage_black'], BL, im, wid, hgt)
    image_maker.run(img_data['gImage_red'], RB, im, wid, hgt)
    im.save('test.png')
