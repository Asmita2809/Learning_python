adj=['red','fresh','tasty']
fruits=['apple','apricot','cherry']
for i in adj:
    print('.............')
    for j in fruits:
        print(i,j)

for i in range(1, 11):
   for j in range(1, 11):
       print(i * j, end=' ') 
   print(' ')

words= ["Apple", "Banana", "Car", "Dolphin" ]
for word in words:
 print ("The following lines will print each letters of "+word)
 for letter in word:
     print (letter)
 print("") 