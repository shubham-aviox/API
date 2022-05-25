# this function return the 30 dates
from datetime import timedelta, datetime, date
import json
from django.views import View

def create_date(any_date):
    # date_time_str=any_date.strftime("%d/%m/%Y")
    total_date=datetime.strptime(any_date, "%d/%m/%Y") + timedelta(days=30)
    print(total_date)

x=input("enter any date: ")
create_date(x)

# create_date = lambda any_date: x + timedelta(days=30)
# any_date=input("enter date: ")
# x = datetime.strptime(any_date, "%d/%m/%Y")
# print(create_date(2/2/2020))

d1={'a.py':'shubh',
	'b.py':'shubh',
	'c.py':'rahul',
}

# d2 = {}
# for key, value in d1.items():
#     if value not in d2:
#         d2[value]=[key]
#     else:
#         d2[value].append(key)
    
# result = json.dumps(d2)

# f=open('d1.txt', 'a')
# f.write(result)
# f.close()

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# d = {}
# for k in keys:
#     for v in values:
#         d[k]=v
#         values.remove(v)
#         break
# # print(d)
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# d=dict(zip(keys, values)) 
# print(d)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

class Demo:
    def __init__(self, name, age, roll):
        self.name= name
        self.age= age
        self.roll= roll

d=Demo("shubh", 27, 12)
print(type(d))

# datetime find date of 30 days after by given a date using lambda and function define
# lambda
# dictionary questions
# convert dictionary in json data and stored in file
# pep8 coding convension
# django models 

class firstClassBasedView(View):
    def show(self):
        print("hello from CBV")

obj = firstClassBasedView()
obj.show()