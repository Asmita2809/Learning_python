def fibonacci_of(n):
    if (n==0 or n==1): #base case 
        return n 
    else: 
      return fibonacci_of(n-1)+fibonacci_of(n-2) #recurssive case

for n in range(15):
     print(fibonacci_of(n)) 
         
 
