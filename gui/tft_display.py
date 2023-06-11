import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from constant.font_constant import FontSize
from constant.color_constant import Colors
from lib.adafruit_rgb_display import st7735

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

BAUDRATE = 24000000

class TFTDisplay(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(TFTDisplay,cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.x=0
        self.y=0
        self.spi = board.SPI()
        self.display = st7735.ST7735R(
            self.spi,
            rotation=90,
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=BAUDRATE)
        if self.display.rotation % 180 == 90:
            self.height = self.display.width  
            self.width = self.display.height
        else:
            self.width = self.display.width  
            self.height = self.display.height
        self.image = Image.new("RGB", (self.width, self.height))
        self.window = ImageDraw.Draw(self.image)
    
    def clear_display(self):
        self.window.rectangle((0, 0, self.width, self.height), outline=0, fill=(0, 0, 0))
        self.show()

    def show(self):
        self.display.image(self.image)
    
    def text(self,value,x,y,font=FontSize.s300,color=Colors.white):
        if x ==None:
            x = self.x
        if y ==None:
            y = self.y
        self.window.text((x, y), value, font=font, fill=color)
        self.y+= font.getsize(value)[1]
        
    def draw_image(self,path="test.jpg"):
        self.img= Image.open(path)
        self.image_ratio = self.img.width / self.img.height
        self.screen_ratio = self.width / self.height
        if self.screen_ratio < self.image_ratio:
            self.scaled_width = self.img.width * self.height // self.img.height
            self.scaled_height = self.height
        else:
            self.scaled_width = self.width
            self.scaled_height = self.img.height * self.width // self.img.width
            self.image = self.img.resize((160,128),Image.BICUBIC)
    
    
        
        
        