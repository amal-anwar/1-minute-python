def findHCF(x,y):
    hcf=0
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller + 1):
     if((x % i == 0) and (y % i == 00)):
         hcf = i
    return hcf

num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
print("HCF = ", findHCF(num1,num2))
