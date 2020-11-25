#
array = []
for i in range(20):
	if i % 2 == 1:
		array.append(i)

array2 = [i for i in range(20) if i % 2 == 1]

print(array)
print(array2)

#
array3 = []
for _ in range(3):
	array3.append([0] * 4)

array4 = [[0] * 4 for _ in range(3)]

print(array3)
print(array4)

#
a = [1, 2, 3, 4, 5, 6]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]
print(result)