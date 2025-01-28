from PIL import Image
import random

dracula = Image.open(r"C:/Users/Ziyad/Downloads/draculaCopy.png")
pixels = dracula.load()

for i in range(0,100):
    x = random.randint(0,200)
    y = random.randint(0,200)
    print(x,y)
    dracula.putpixel((x,y),(0,0,0))

dracula.show()

dracula = Image.open(r"C:/Users/Ziyad/Downloads/draculaCopy.png")
pixels = dracula.load()

dracula.save(r"C:/Users/Ziyad/Downloads/draculaAltered.png")