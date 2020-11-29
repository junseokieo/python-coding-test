n = int(input())
data = input().split()

x = 1
y = 1
for elem in data:
	if elem == 'L' and x > 1:
		y -= 1
	elif elem == 'R' and x < n - 1:
		y += 1
	elif elem == 'U' and y > 1:
		x -= 1
	elif elem == 'D' and y < n - 1:
		x += 1
print('%d %d' % (x, y))