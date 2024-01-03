binary= input("enter a binary no")
def binarytodecimal(binary):
    decimal=0
    for digits in binary:
        decimal=decimal*2 +int(digits)
    print("the decimal value of the binary number:",binary,"is",decimal)
binarytodecimal(binary)

