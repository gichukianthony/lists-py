my_list = []#creating an empty list
#appending/adding 10,20,30 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.insert(1, 15)#aadding 15 at index 1
my_list.extend([50, 60, 70])#adding multiple values to the list
my_list.pop()#removing the last element
my_list.sort()
index_30 = my_list.index(30)  # Find index of value 30
print("Sorted List:", my_list)
print("Index of 30:", index_30)#printing the index of 30