
#Question 1 : Create an empty list called my_list
my_list=list()

#Question 2:Append the following elements to my_list: 10, 20, 30, 40.
for value in [10,20,30,40]:
 my_list.append(value)
print(my_list)

#Question 3:Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(my_list)

#Question 4:Extend my_list with another list: [50, 60, 70] 
my_list2=[50,60,70]
my_list.extend(my_list2)
print(my_list)

#Question 5: Remove the last element from my_list.
my_list.pop(-1)
print(my_list)

#Question 6: Remove the last element from my_list.
my_list.sort()
print(my_list)

#Question 7: Find and print the index of the value 30 in my_list
index_of_30=my_list.index(30)
print(index_of_30)