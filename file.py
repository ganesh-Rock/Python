import json
from datetime import datetime
import time
import random
# Opening JSON file
f = open('/home/OhmGanesh/Downloads/training_data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
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
        if("-" not in i['impact_factor']):
            lst.append(float(i['impact_factor']))
# Closing file
x1=max(lst)

for i in data:
    if ("-" not in i['impact_factor']):
        if(float(i['impact_factor'])==x1):
            lst1.append(i)



random_num = random.choice(lst1)
print(random_num)
f.close()