import requests as http 

class Client():
    def __init__(self) -> None:
        pass
    def get(self,url,params={},headers={}):
        resp = http.get(url,params=params,headers=headers)
        print(resp.status_code)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None
    def post(self,url,params={},headers={}):
        resp = http.post(url,params=params,headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None                                                     


