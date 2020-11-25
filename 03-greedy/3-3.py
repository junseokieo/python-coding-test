n, m = map(int, input().split())

result = 0

for i in range(n):
	data = list(map(int, input().split()))
	min_data = min(data)
	result = max(min_data, result)

print(result)

# 답안과 유사하여 answer 파일을 작성하지 않았습니다