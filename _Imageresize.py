from pylab import *
from PIL import Image

def imresize(image,size):
    pil_im = Image.fromarray(uint8(image))

    return array(pil_im.resize(size))