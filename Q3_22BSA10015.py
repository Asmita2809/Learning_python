#program for printing prime numbers between 100 and 200
for num in range(100,201):
     for i in range(2, int(num**0.5)+1):
        #checking if the number is divisible by any integer from 2 to half the number 
        if(num %i == 0):
            break
     else:
        #if the loop continues without break the no is prime
        print(num)