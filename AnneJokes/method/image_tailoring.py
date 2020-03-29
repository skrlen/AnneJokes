from PIL import Image
from io import BytesIO


def make_thumb(img, name, size=(64, 64)):
    """
    生成指定大小的缩略图,   暂时无用
    :param size: 指定尺寸
    :return:
    """
    im = Image.open(BytesIO(img))
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255 - x)
            im = im.convert('RGB')
            im.paste((255, 255, 255), None, bgmask)

        else:
            im = im.convert('RGB')

    width, height = im.size
    if width == height:
        region = im
    else:
        if width>height:
            delta = (width - height) / 2
            box = (delta, 0, delta+height, height)
        else:
            delta = (height-width) / 2
            box = (0, delta, width, delta+width)
        region = im.crop(box)
    thumb = region.resize((size[0], size[1]), Image.ANTIALIAS)
    thumb.save(name, quality = 100)
