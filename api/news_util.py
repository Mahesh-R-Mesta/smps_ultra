from api.api_helper import Client
from constant.api_constant import URL


class NewsApi():
    def __init__(self) -> None:
        self.client = Client()
    def in_short(self,category):
        data = self.client.get(URL.in_short_news,{"category": category})
        if data != None:
            return data
    def space_flight(self):
        data = self.client.get(URL.space_news)
        if data !=None:     
            return data
    def weather(self,location="sirsi"):
        data = self.client.get(URL.weather.join(location))
        if data !=None:
            return data
    def jokes(self):
        data = self.client.get(URL.jokes)
        if data !=None:
            return data
    






 