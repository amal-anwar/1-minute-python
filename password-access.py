passwordFile = open("SecretPasswordFile.txt","w")#w Opens a file for writing, creates the file if it does not exist
passwordFile.write('blue')
passwordFile.close()

passwordFile = open("SecretPasswordFile.txt","r")#r Opens a file for reading, error if the file does not exist
secretPassword = passwordFile.read()

print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
if typedPassword == '12345':
    print('That password is one that an idiot puts on their luggage.')
if typedPassword != secretPassword:
    print('Acess Denied')
