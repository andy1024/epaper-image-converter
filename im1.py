from PIL import Image
import ximage

#apply a single layer of image defined as hex stream
#intended to be run on an e-paper screen
#it draws from right to left, from bottom to the top
#splitting each byte
#into eight pixels
def run(data, color, im, wid, hgt):
    x=wid-1
    y=0
    #c=0
    try:
        for byte in data:
            #print(byte)
            for bit_index in range(7,-1,-1):
                bit = ( byte >> bit_index ) & 1
                #print(bit)
                if not bit:
                    #im.putdata([255,255,0])
                    im.putpixel( (x,y), color)
                #else:
                    #im.putdata([0,255,255])
                y += 1
                if y >= hgt:
                    y = 0
                    x -= 1
                    if x <= 0:
                        raise Exception
            #c += 1
            #print(c)
    except:
        pass
    
if __name__ == "__main__":
    wid = 212
    hgt = 104
    BL=(0,0,0)
    RB=(255,0,0)
    im=Image.new('RGB', (wid, hgt), color=(255,255,255,0))
    #im.putdata([(255,0,0), (0,255,0), (0,0,255)])
    run(ximage.black, BL, im, wid, hgt)
    run(ximage.red, RB, im, wid, hgt)
    im.save('test.png')
