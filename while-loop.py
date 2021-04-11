#password guessing using while loop
password = "amal"
guess = ""
while (password!= guess):
    guess = input ("Enter password: ")
    if password == guess:
        print ("Login successful")
    else:
        print("Incorrect password. Try again.")
