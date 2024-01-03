#create a list of integers
my_list=[3,5,2,1,18,7]

#print the original list
print("original list:", my_list)

#add an element to the list
my_list.append(4)

#print the updated list
print("list after adding an element: ",my_list)

#sort the list in ascending order
my_list.sort()

#print the sorted list
print("list after sorting:",my_list)

#use the same list as an array to find the largest number in the given array
largest_num=my_list[-1] #last element in the list is the largest number
print("the largest number in the given array is: ",largest_num)