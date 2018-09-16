import copy
list1 =[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
list2 = copy.copy(list1)

print("Output of Shallow Copy : ")
list2[1][2] = 9
print(list1)
print(list2)

print("Output of Deep Copy : ")
list3 = copy.deepcopy(list1)
list3[0][1] = 23
print(list1)
print(list3)
