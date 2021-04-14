total = 0 #global variable

def sum(arg1,arg2):
    "Add both the parameters and return them."
    total=arg1+arg2
    print("Inside the function local total: ",total)
    return total

sum( 10, 20)
print("Outside the function total: ",total)

Inside the function local total:  30
Outside the function total:  0
>>> 
