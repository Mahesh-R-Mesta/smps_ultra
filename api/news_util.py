from api.api_helper import Client
from constant.api_constant import URL
from lib.tft_display import TFTDisplay
from constant.font_constant import FontSize
from constant.color_constant import Colors

class NewsApi():
    def __init__(self) -> None:
        self.client = Client()
        self.tft = TFTDisplay()
    def in_short(self,category):
        data = self.client.get(URL.in_short_news,{"category": category})
        if data != None:
           return data
    def space_flight(self):
        data = self.client.get(URL.space_news)
        print(data)
        if data !=None:
            self.tft.clear_display()
            self.tft.text(str(data),font=FontSize.s200,color=Colors.blue)
            self.tft.show()    
            return data
    def weather(self,location="sirsi"):
        data = self.client.get(f'{URL.weather}{location}')
        if data !=None:
            return data
 
    






 