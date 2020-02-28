"""
绘图模块
"""
from PIL import Image, ImageDraw, ImageFont
import random, io
from Anne.settings import FONT
import base64


def verify():
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    height = 20
    imgobj = Image.new('RGB', (width, height), bgcolor)
    draw = ImageDraw.Draw(imgobj)

    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill)

    str1 = "AB4CDE6FGH5IJKLM3N2O1PQR9S7TUV8WXYZ0"
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    font = ImageFont.truetype(FONT, 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)

    del draw
    f = io.BytesIO()
    imgobj.save(f, 'png')
    base64_str = base64.b64encode(f.getvalue())
    return rand_str, base64_str

