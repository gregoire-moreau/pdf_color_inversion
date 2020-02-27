import fitz
from PIL import Image


def invert(doc):
    images = []
    for i in range(doc.pageCount):
        page = doc.loadPage(i)
        mat = fitz.Matrix(2, 2)
        img = page.getPixmap(matrix=mat)
        img.invertIRect()
        images.append(Image.frombytes("RGB", [img.width, img.height], img.samples))
    return images
