import json
from datetime import datetime
import time
import random

f = open('/home/OhmGanesh/Downloads/training_data.json')
data = json.load(f)
val = input("Enter your value: ")
year = time.strftime("%Y") # or "%y"
x=int(year)-int(val)
print(x)
lst = []
lst1 =[]
for i in data:
    datestring = i['pub_date']
    dt = datetime.strptime(datestring, '%Y-%m-%d')
    if(dt.year==x):
        lst.append(i['impact_factor'])

x1=max(lst)

for i in data:
   if(i['impact_factor']==x1):
            lst1.append(i)


random_num = random.choice(lst1)
print(random_num)
f.close()