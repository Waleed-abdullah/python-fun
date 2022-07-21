from distutils.command import clean
import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    cleanName = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    img.save(f'{directory}/{cleanName}.png', 'png')

print('All Done!')
