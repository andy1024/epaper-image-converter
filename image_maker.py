from PIL import Image
import const_reader

#apply a single layer of image defined as hex stream
#intended to be run on an e-paper screen
#it draws from right to left, from bottom to the top
#splitting each byte
#into eight pixels
def run(data, color, im, wid, hgt):
    x=wid-1
    y=0
    try:
        for byte in data:
            for bit_index in range(7,-1,-1):
                bit = ( byte >> bit_index ) & 1
                if not bit:
                    im.putpixel( (x,y), color)
                y += 1
                if y >= hgt:
                    y = 0
                    x -= 1
                    if x <= 0:
                        raise Exception
    except:
        pass
    
if __name__ == "__main__":
    wid = 212
    hgt = 104
    BL=(0,0,0)
    RB=(255,0,0)
    im=Image.new('RGB', (wid, hgt), color=(255,255,255,0))
    with open("image.h") as infile:
        contents = infile.read()
        img_data = const_reader.read_consts(contents)
    #print(img_data)
    run(img_data['gImage_black'], BL, im, wid, hgt)
    run(img_data['gImage_red'], RB, im, wid, hgt)
    im.save('test.png')
