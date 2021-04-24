"""import random 
import string


chars =string.printable

password = random.choice(chars)

print("Here is your random character - ",password)"""

import random 
import string


length = int(input("State the length of password in numbers\n>>> "))

password_chars =string.printable

password = []

for x in range (length):
    password.append(random.choice(password_chars))
print("Here is your random password - ",''.join(password))
