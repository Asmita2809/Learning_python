num= 1234456789
rev=0
while(num>0):
  rev=(rev*10)+(num%10)
  num=num//10
print("the reversed no is :",rev)
