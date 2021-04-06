#the following is to check the starting of the string
>>> 'hello'.startswith('he')
True
>>> 'hello'.startswith('vvvv')
False
>>> 'hello'[:3]=='hel' #3 indicates first three letters of the string
True
>>> 'hello'[:2]=='he' #2 indicates first two letters of the string
True
>>> 'hello'[:2]=='xv'
False
