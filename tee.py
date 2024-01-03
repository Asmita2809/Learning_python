# def gcd(a,b):
#     r=a%b
#     while(r!=0):
#         a=b
#         b=r
#         r=a%b
#     return b
# print(gcd(5,10)) 
import random
# print(random.randrange(10))
# print(random.randrange(10, 20))
# print(random.randrange(100, 200, 2))

# print(random.randrange(5, 480, 3))
# name = "Programming_in_Python"
# new_name = random.sample(name, k = 2)
# print(name, new_name)
# a=[1,2,4,1,3,6]
# # a.pop(2)
# a.reverse()
# print(a)

# a={2,6,8,4}
# b={1,3,2,5,9}
# print(a.difference(b))
# a="ydryfhg ugvj gvjbh"
# print(a.split())
decimal= input("dwnk")
def DecimalToBinary(decimal):
    if decimal > 1:
       DecimalToBinary(decimal // 2)
    print(decimal % 2, end='')
print('the Binary value of the decimal no.', decimal , 'is: ' , end='')

# Calling the function

DecimalToBinary(int(decimal))
