from api.news_util import NewsApi
from api.insta_util import InstaApi
from dotenv import load_dotenv
from gui.tft_display import TFTDisplay
from constant.font_constant import FontSize
from constant.color_constant import Colors
import services.scheduler 
load_dotenv(".env")

#news = NewsApi()
#insta = InstaApi() 
#insta.set_username('_bachuuuu')
#insta.get_posts(count=20)
# print(news.in_short('politics'))
#print(news.space_flight())
#print(news.weather())

tft = TFTDisplay()

tft.clear_display()
tft.text("Hello World")
tft.text("Hello World",font=FontSize.s300,color=Colors.blue)
tft.show()