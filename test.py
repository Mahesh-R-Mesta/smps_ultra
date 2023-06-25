from api.news_util import NewsApi
from api.insta_util import InstaApi
from dotenv import load_dotenv
from lib.tft_display import TFTDisplay
from constant.font_constant import FontSize
from constant.color_constant import Colors
import services.scheduler 
load_dotenv(".env")

news = NewsApi()
#insta = InstaApi() 
#insta.set_username('_bachuuuu')
#insta.get_posts(count=20)
# print(news.in_short('politics'))
# news.space_flight()
#print(news.weather())

tft = TFTDisplay()

tft.clear_display()
tft.text("Completed task")
tft.text("1) Testing name",font=FontSize.s200,color=Colors.blue)
tft.text("2) inno script",font=FontSize.s200,color=Colors.white)
tft.text("3) table management",font=FontSize.s200,color=Colors.pink)
tft.show()