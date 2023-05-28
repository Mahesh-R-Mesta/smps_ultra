from api.news_util import NewsApi
from dotenv import load_dotenv

config = load_dotenv(".env")
news = NewsApi()

print(news.in_short('politics'))
print(news.space_flight())
print(news.jokes())