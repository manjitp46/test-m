import datetime
import calendar
import random

data = dict()
i= 0
for i in range(5):
    data[i] = random.randint(1,101)


for k,v in data.items():
    print(k,v)    