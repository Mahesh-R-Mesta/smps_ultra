from PIL import ImageFont


class FontSize():
    _path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    s100 = ImageFont.truetype(_path,5)
    s200 = ImageFont.truetype(_path,10)
    s300 = ImageFont.truetype(_path,15)
    s350 = ImageFont.truetype(_path,17)
    s400 = ImageFont.truetype(_path,20)
    s450 = ImageFont.truetype(_path,22)
    s500 = ImageFont.truetype(_path,24)