# A Python program to return multiple  
# values from a method using class 
class Test: 
    def __init__(self): 
        self.str = "amal"
        self.x = 20   
  
# This function returns an object of Test 
def function(): 
    return Test() 
      
# Driver code to test above method 
t = function()  
print(t.str) 
print(t.x) 
