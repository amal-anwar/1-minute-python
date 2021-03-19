#a simple program 
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
'''
will give the output 9
'''
#program to find days till christmas 
from datetime import date
today = date.today ()
christmas = date(date.today().year, 12,25)
until_christmas = christmas - today

'''
>>> until_christmas
datetime.timedelta(days=281)
>>> until_christmas.days
281
'''
