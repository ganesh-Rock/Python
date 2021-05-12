#!/bin/python3

# system packages
import sys
import json
import time
import random
from datetime import datetime
import urllib.request

# Third party packages
from TwitterAPI import TwitterAPI


class Twiiter:
    def randomjoice(self, list):

        random1=random.choice(list)
        print(random1)
        status = urllib.request.urlopen(random1['html_url']).getcode()

        if(status==200):
            return random1
        else:
            list.remove(random1)
            self.randomjoice(list)


    def biggiest_one(self, f):

        data = json.load(f)
        val = input("Enter your value: ")
        year = time.strftime("%Y")
        x = int(year) - int(val)
        print(x)

        lst = list()
        lst1 = list()
        lst2 = list()

        for i in data:
            lst2.append(i['pub_date'])

        date1=min(lst2)
        dt1 = datetime.strptime(date1, '%Y-%m-%d')
        if(dt1.year>x):
            print("NO DATA IN THIS YEAR")
            print(f"Starting Year is {dt1.year}")
            x = dt1.year


        for i in data:
            datestring = i['pub_date']
            dt = datetime.strptime(datestring, '%Y-%m-%d')

            if (dt.year == x):
                lst.append(i['citation_count'])
        x1 = max(lst)

        if(int(x1)==0):
            for i in data:
                lst1.clear()
                datestring = i['pub_date']
                dt = datetime.strptime(datestring, '%Y-%m-%d')
                if (dt.year == x):

                    lst.append(i['impact_factor'])

            x1 = max(lst)


        for i in data:
            datestring = i['pub_date']
            dt = datetime.strptime(datestring, '%Y-%m-%d')

            if (dt.year == x):

                if (i['impact_factor'] == x1):
                    lst1.append(i)
        print(lst1)
        random=self.randomjoice(lst1)
        return random

    def twitter_call(self, article, recipient_id):

        api = TwitterAPI('0FhLyMVeriLhHqvSgRuAyXhMq',
                         'oDGV6dWmUQtQbJJiMM2E22JZQTTfVd5ZKlFhl6ifWJ42fvAyB0',
                         '1390159632975290371-o8BnA9kodSfDlt8yLI4ZBBT5qeXsmy',
                         'ttqnGINBOZSWr6f2nUXPGMQYxs7zQK35fxdqtBOIyk0Gn')

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
    # this would threw the big article in the json file
    output_one = twitter_obj.biggiest_one(input_file)

    print(output_one)

    # sending the tweet form a particular one
    twitter_obj.twitter_call(output_one, user_id)