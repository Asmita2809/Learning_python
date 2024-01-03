x=False
print(bool(x))
print(bool())
#in 'and' we check 2nd condition only when 1st condition is true 
# else we dont check the 2nd condition

#in 'or' the 2nd condition is checked only when ist cond. is false


n=int(input('n= '))
i=1
while (i<=n):
    print(n,'x',i,'=',n*i)
    i=i+2
print('done')

i=1
while i<6:
    print(i)
    i+=1

fruits=['apple','banana','mango','cherry','apricot']
for i in fruits:
    print(i)
    
for x in 12345:
    print(x)