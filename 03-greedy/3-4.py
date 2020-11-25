n, k = map(int, input().split())

count = 0

while n != 1:
	if n % k == 0:
		n /= k
		count += 1
		continue
	n -= 1
	count += 1

print(count)

# 최대한 많이 나누기를 해야 한다. 왜? "2 이상의 수로 나누는 것이 1을 빼는 것보다 숫자를 훨씬 많이 줄일 수 있어서!" -> 매우 논리적