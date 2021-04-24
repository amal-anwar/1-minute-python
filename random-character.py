import random 
import string


chars =string.printable

password = random.choice(chars)

print("Here is your random character - ",password)
