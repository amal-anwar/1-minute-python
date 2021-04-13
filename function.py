def greet (name):
    print("Hello,  " + name + ". Good morning.")

>>> greet ('Amal')
Hello,  Amal. Good morning.
>>> 
______________________________________________________________
def add(x,y):
    
    sum = x + y
    return sum
    
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The sum is: ", add(num1,num2))

Enter a number: 1
Enter another number: 2
The sum is:  3
>>>
__________________________________________________________
def printInfo(name, **marks ):
    print ("Marks of ", name)
    for subject, mark in marks.items():
        print(subject, "-", mark)
    return
printInfo("Amal", English=99,Maths=98)

