from PIL import Image


def make_thumb(path, size=150):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if height > size:
        delta = height / size
        width = int(width / delta)
        pixbuf.thumbnail((width, height), Image.ANTIALIAS)
        return pixbuf
