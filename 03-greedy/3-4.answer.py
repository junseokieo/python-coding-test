n, k = map(int, input().split())
result = 0

while True:
	target = (n // k) * k # n이 여기까지 빼져야 됨
	result += (n - target) # 그 횟수를 한번에 더함
	n = target
	if n < k:
		break
	result += 1
	n //= k

result += n - 1
print(result)