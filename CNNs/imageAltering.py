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
from PIL import Image
import random

dracula = Image.open(r"C:/Users/Ziyad/Downloads/draculaCopy.png")
pixels = dracula.load()

for i in range(0, 100):
    x = random.randint(0, dracula.width - 1)
    y = random.randint(0, dracula.height - 1)
    print(x, y)
    dracula.putpixel((x, y), (0, 0, 0))

dracula.save(r"C:/Users/Ziyad/Downloads/draculaAltered.png")