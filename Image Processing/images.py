from PIL import Image, ImageFilter
import os

img = Image.open("p.jpg")
filteredImage = img.filter(ImageFilter.DETAIL)
filteredImage.show()
