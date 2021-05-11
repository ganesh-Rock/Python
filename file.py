#!/bin/python3

#system packages
import sys
import json
import time
import random
from datetime import datetime

#Third party packages
from TwitterAPI import TwitterAPI

class Twiiter:

    def biggiest_one(self, f):

        data = json.load(f)
        val  = input("Enter your value: ")
        year = time.strftime("%Y")
        x    = int(year) - int(val)
        
        lst  = list()
        lst1 = list()
        

        for i in data:
            datestring = i['pub_date']
            dt = datetime.strptime(datestring, '%Y-%m-%d')

            if(dt.year==x):
                lst.append(i['impact_factor'])

        x1 = max(lst)

        for i in data:
            datestring = i['pub_date']
            dt = datetime.strptime(datestring, '%Y-%m-%d')
            
            if (dt.year == x):
                
                if(i['impact_factor']==x1):
                        lst1.append(i)


        return random.choice(lst1)


    def twitter_call(self, article, recipient_id):

        api = TwitterAPI('Y9VkZFCua2lFUnkTBvC8Jit1F',
                        'rC6w28rVMHhbHhqGnUpkUlloiXFBIuTpEiNBpxOPJJzZKVjlQL',
                        '1390159632975290371-3LjIRKz9akHp2svstaC28ZIMREvOPC',
                        '9oXkNQcHU3wWiGtoCiArgYmRI67ilTGKsvHWaRrzCVZrZ')
        
        message_text = json.dumps(article)

        event = {
            "event": {
                "type": "message_create",
                "message_create": {
                    "target": {
                        "recipient_id": recipient_id
                    },
                    "message_data": {
                        "text": message_text
                    }
                }
            }
        }

        r = api.request('direct_messages/events/new', json.dumps(event))
        print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)


if __name__ == '__main__':

    input_file = open(sys.argv[1])
    user_id = "1390159632975290371"
    
    twitter_obj = Twiiter()
    #this would threw the big article in the json file
    output_one = twitter_obj.biggiest_one(input_file)

    print(output_one)

    #sending the tweet form a particular one
    twitter_obj.twitter_call(output_one, user_id)




    





