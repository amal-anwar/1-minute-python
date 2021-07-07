a = '2'
b = '3'
  
# convert a using int 
a = int(a) 
  
# convert b using int 
b = int(b) 
  
# sum both integers 
sum = a + b 
  
# as strings and integers can't be added 
# test the sum 
print(sum) 

_____________________________________________

ui_input = input("Enter a string between one and five - ");
ui_input = ui_input.lower ()
if ui_input == 'one':
    print(1)
elif ui_input == 'two':
    print(2)
elif ui_input == 'three':
    print(3)
elif ui_input == 'four':
    print(4)
elif ui_input == 'five':
    print(5)
else:
    print ('Out of range')
