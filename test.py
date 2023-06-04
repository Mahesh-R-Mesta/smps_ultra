from api.news_util import NewsApi
from api.insta_util import InstaApi
from dotenv import load_dotenv
import services.scheduler 
load_dotenv(".env")

news = NewsApi()
insta = InstaApi() 
insta.set_username('_bachuuuu')
insta.get_posts()
print(news.in_short('politics'))
print(news.space_flight())
print(news.weather())