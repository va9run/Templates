from PIL import Image

def openimage(location,name):
    img = Image.open(location+"/"+name)
    img.show()