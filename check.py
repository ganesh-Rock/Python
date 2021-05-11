from TwitterAPI import TwitterAPI
import json
from datetime import datetime
import time
import random
from file import biggiest_one
from file import twitter_call



f = open('/home/OhmGanesh/Downloads/training_data.json')
data = json.load(f)
val = input("Enter your value: ")
year = time.strftime("%Y") # or "%y"
x=int(year)-int(val)
print(x)
lst = []
lst1 =[]
lst2  =[]
for i in data:
    datestring = i['pub_date']
    dt = datetime.strptime(datestring, '%Y-%m-%d')
    if(dt.year==x):
        lst.append(i['impact_factor'])
        lst1.append(i)
x1=max(lst)
print(x1)
for i in lst1:
    if(i['impact_factor']==x1):
        lst2.append(i)

for i in lst1:
    print(i['pub_date'])
    print(i['impact_factor'])


print("**********************************************************************************************************************************8")

for i in lst2:
    print(i['pub_date'])
    print(i['impact_factor'])
random_num = random.choice(lst2)
print(type(random_num))
api = TwitterAPI('Y9VkZFCua2lFUnkTBvC8Jit1F',
                 'rC6w28rVMHhbHhqGnUpkUlloiXFBIuTpEiNBpxOPJJzZKVjlQL',
                 '1390159632975290371-3LjIRKz9akHp2svstaC28ZIMREvOPC',
                 '9oXkNQcHU3wWiGtoCiArgYmRI67ilTGKsvHWaRrzCVZrZ')

user_id = "1390159632975290371"
message_text = json.dumps(random_num)

event = {
    "event": {
        "type": "message_create",
        "message_create": {
            "target": {
                "recipient_id": user_id
            },
            "message_data": {
                "text": message_text
            }
        }
    }
}

r = api.request('direct_messages/events/new', json.dumps(event))
print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)

f.close()