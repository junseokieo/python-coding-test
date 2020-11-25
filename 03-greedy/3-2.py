n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0
cnt = 0

for i in range(m):
	if cnt == k:
		result += second
		cnt = 0
		continue
	result += first
	cnt += 1

print(result)