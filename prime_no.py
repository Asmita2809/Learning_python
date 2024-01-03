n=int(input('enter any no:'))
if n>1:
 for i in range(2,n//2+1):
    if(n%i==0):
        print(n,' is not prime')
        break
 else:
        print(n,' is prime')
else:
    print(n,'is not prime')
