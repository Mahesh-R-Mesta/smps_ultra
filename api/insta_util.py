from api.api_helper import Client
from constant.api_constant import InstaUrl
import instaloader 
import os

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Referer": "https://www.instagram.com/",
        "x-csrftoken": "NlOg81B9gUTJnrAWU9FKuPVv9P4JZY9x",
        "cookie":f"sessionid={os.getenv('INSTA_SESSION')}"
}



class InstaApi():
    def __init__(self) -> None:
        self.client = Client()
        self.loader = instaloader.Instaloader()
        # self.username = os.getenv('USER_NAME')
        # self.passw = os.getenv('USER_PASS')
        # print(self.username)
        # print(self.passw)
        # self.loader.login(self.username,self.passw)
        # self.session = os.getenv('INSTASESSION')
    def getByUsername(self,username):
        user = instaloader.Profile.from_username(self.loader.context,username=username)
        if user!=None:
            return user
    def get_image_user(self,username):
        user = self.loader.download_profile(username,profile_pic_only=True)
        print(user)
    def search(self,username):
        data = self.client.get(InstaUrl.searchUser,{
                'context':'blended',
                'query': username,
                'rank_token': 0.3708183727469332,
                'include_reel':True
        },headers=headers)
        if data!=None:
            return data
    


    