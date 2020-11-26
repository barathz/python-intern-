#Creating The List
my_list = list()
#appending elements into the list 
my_list.append(6)
my_list.append(5)
my_list.append(1)
my_list.append(8)
my_list.append(9)

# Remove the last element from the list
my_list.pop()
#Remove the specific element
my_list.remove(6)
#Max num from the list 
maximum = max(my_list)
print(f"Maximum number from the list is {maximum}")
#Min num from the list 
minimum = min(my_list)
print(f"Minimum number from the list is {minimum}")

print(my_list)

#create tuple
my_tuple = ('x','d','f','v','q','y','c')

print(my_tuple[::-1])

#converting tuple into list
my_list1 = list(my_tuple)
print(my_list1)
