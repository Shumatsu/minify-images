import os
from PIL import Image

inPath = os.path.join(os.path.dirname(__file__), 'input')

for filename in os.listdir(inPath):
    img = Image.open(os.path.join(inPath, filename))
    img = img.convert('RGB')
    filename = '1_' + os.path.basename(filename)
    outFile = os.path.join(os.path.dirname(__file__), 'output', filename)
    img.save(outFile, format='jpeg', optimize=True, quality=85)
