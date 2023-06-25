from api.api_helper import Client
from constant.api_constant import InstaUrl
import instaloader 
import os
from lib.tft_display import TFTDisplay
from constant.font_constant import FontSize
from constant.color_constant import Colors

    
class InstaApi():
    def __init__(self) -> None:
        self.client = Client()
        self.loader = instaloader.Instaloader()
        self.path = 'insta_data'
        self.tft = TFTDisplay()
    def login(self):
        self.username = os.getenv('USER_NAME')
        self.password = os.getenv('USER_PASS') 
        self.loader.login(self.username,self.password)
    
    def set_username(self,username):
        self.user = instaloader.Profile.from_username(self.loader.context,username=username)
        if self.user!=None:
            return self.user
    def show_user(self):
        if self.user!=None:
            self.tft.clear_display()
            self.tft.text(f'name: {self.user.full_name}',font=FontSize.s300,color=Colors.white)
            self.tft.text(f'follower: {self.user.followers}',font=FontSize.s200,color=Colors.white)
            self.tft.text(f'followees: {self.user.followees}',font=FontSize.s200,color=Colors.white)
            self.tft.text(f'bio: {self.user.biography}',font=FontSize.s200,color=Colors.white)
    def get_posts(self,count=5):
        i=0
        for post in  self.user.get_posts():
            
            self.loader.download_post(post,target=self.path)
            i+=1
            if i > count:
                break
        
    def get_image_user(self,username):
        self.loader.download_profile(username,profile_pic_only=True)


    