def oct(n):
    print('pased octal number is ',n)
    num =str(n)
    decnum =int(num,8)
    print('Number in decimal : ',decnum)
    print("Number in binary : ", bin(decnum))
    print("Number in Hexa Decimal : ",hex(decnum))
num = int(input("Enter an Octal Number : "))
oct(num)