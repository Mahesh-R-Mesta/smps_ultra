import schedule
from datetime import datetime
import os
import json



def birth_day():
    with open(os.getcwd()+"//data//birthday.json",'r') as file:
        data = json.loads(file.read())
        today = datetime.now()
        for birthday in data['birthday']:
            birth_date = datetime.fromisoformat(birthday['date'])
            if today.day == birth_date.day and today.month == birth_date.month:
                return birthday



print(birth_day())



# schedule.every().at("9:00").do(birth_day)