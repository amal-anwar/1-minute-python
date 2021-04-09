l = ["a", "b","cdef"]
print("".join(l)) 

#prints abcdef as the output

l = ["a", "b","cdef"]
print(','.join(l)) 

#prints a,b,cdef as the output

l = ["a", "b","cdef"]
for x in range(len(l)): #using for loop
    print (l[x])
    
"""
prints 
a
b
cdef
as the output
"""

>>> list6 = ['amal', 24, 2.24, 'red', 68.4]
>>> list7 = [14,'blue']

>>> print (list6)
['amal', 24, 2.24, 'red', 68.4]

>>> print(list6[0]) #prints first element of list
amal

>>> print(list6[1:3]) #prints elements starting from 2nd till 3rd
[24, 2.24]

>>> print(list6[2:]) #prints elements starting from 3rd element
[2.24, 'red', 68.4]

>>> print (list7*2) #prints list twice
[14, 'blue', 14, 'blue']

>>> print (list6 + list7) #prints concatenated list
['amal', 24, 2.24, 'red', 68.4, 14, 'blue']
