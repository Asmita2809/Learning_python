# def gcd(a,b):
#  r=a%b
#  while (r!=0):
#      a=b
#      b=
#      r=a%b
#  return b

# print(gcd(10764,2300))

# print(hex(14))
#print(dict('asdf',))
#print(sum({1: "one", 2: "two", 3: "three"}.values()))
# x=24.65
# print(floor(x))

import array as my_array

new_arr=my_array.array('i',[10,20,30,40])
print("Original Array is :",new_arr)

#res_arr=my_array.array('i',reversed(new_arr))
a=my_array.array('b',reversed(new_arr))
res_arr=new_arr[::-1]
print("Resultant Reversed Array:",res_arr)
print(new_arr)
res_arr=new_arr[::-1]
