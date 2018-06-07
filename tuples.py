list_1 = ["PHP", "Exercises", "Backend"]
list_2 = []

for i in range(0,len(list_1)):
    list_2.append(len(list_1[i]))


list_3 = []
print(list_2)

tuple_1 = tuple(list_1)
tuple_2 = tuple(list_2)

print(tuple_1)
print(tuple_2)

for i in range(0,len(tuple_1)):
    tuple_3 = (tuple_2[i], tuple_1[i])
    list_3.append(tuple_3)
print(list_3)
list_3.sort()
print(list_3)
a = len(list_3)
print("longest one in the group is: " ,list_3[a-1])