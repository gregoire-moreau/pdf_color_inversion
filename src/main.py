import fitz
import sys
from PIL import Image

images = []
doc = fitz.open(sys.argv[1])
for i in range(doc.pageCount):
    page = doc.loadPage(i)
    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    img = page.getPixmap(matrix=mat)
    img.invertIRect()
    images.append(Image.frombytes("RGB", [img.width, img.height], img.samples))
name = doc.metadata['title']
doc.close()
if len(images) > 1:
    images[0].save('output/%s.pdf'%name, save_all=True, append_images=images[1:])
else:
    images[0].save('output/%s.pdf' % name)
