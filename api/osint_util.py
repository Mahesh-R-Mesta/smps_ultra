from api.api_helper import Client
from constant.api_constant import URL
import os



class OSINT():
    def __init__(self):
        self.client = Client()
        self.token = os.getenv('NUM_TOKEN')
    def search_number(self,number):
        param = {'countryCode': 'in', 'q': number}
        try:
            resp = self.client.get(URL.truecaller,
                params=param,
                headers=self.get_header())
            print(resp.status_code)
            if resp.status_code == 200:
                data = resp.json()
                print(resp.status_code)
            else:
                print(f'Failed to perform task: S-{resp.status_code}')
        except:
            print('some error occured')

    def get_header(self):
        _header = {
            'Host': 'asia-south1-truecaller-web.cloudfunctions.net',
            'Connection': 'keep-alive'
        }
        if self.token!=None :
            _header.update('Authorization',f'Bearer {self.ftoken}')
        return _header