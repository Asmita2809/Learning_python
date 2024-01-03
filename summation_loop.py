def sum_numbers(numbers):
    total=0
    for number in numbers:
      total=total+number
    print(total)

print(sum_numbers([1,2,3,4,5])) #list is considered as a single entity
#pythonic solutions for direct python solutions(functions)

print(sum([1,2,3,4,5])) #list
print(sum((1,2,3,4,5)))#tuple
print(sum({1,2,3,4,5}))#set
print(sum(range(1,6))) #range
print(sum({1:"one",2:"two",3:"three"})) #dictionary
print(sum({1:"one",2:"two",3:"three"}.keys()))

