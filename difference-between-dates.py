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
