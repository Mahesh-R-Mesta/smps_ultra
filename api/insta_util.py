from api.api_helper import Client
from constant.api_constant import InstaUrl
import instaloader 
import os


    
class InstaApi():
    def __init__(self) -> None:
        self.client = Client()
        self.loader = instaloader.Instaloader()
        self.path = 'insta_data'

    def login(self):
        self.username = os.getenv('USER_NAME')
        self.password = os.getenv('USER_PASS') 
        self.loader.login(self.username,self.password)
    
    def set_username(self,username):
        self.user = instaloader.Profile.from_username(self.loader.context,username=username)
        if self.user!=None:
            return self.user
    
    def get_posts(self,count=5):
        i=0
        for post in  self.user.get_posts():
            self.loader.download_post(post,target=self.path)
            i+=1
            if i > count:
                break
        
    def get_image_user(self,username):
        self.loader.download_profile(username,profile_pic_only=True)


    