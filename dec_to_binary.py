decimal=input("enter a decimal number:")
def decimaltobinary(decimal):
    if decimal>1:
        decimaltobinary(decimal//2)
    print(decimal%2,end='')


print('the binary value of the decimal no.',decimal,'is',end=' ')

decimaltobinary(int(decimal))

#we don't reverse it as in resursion there is backtracking and the
#the output is always in reverse order