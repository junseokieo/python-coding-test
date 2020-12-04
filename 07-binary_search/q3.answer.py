# 205쪽.
# 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 구현하지 않고
# 반복문을 이용해 구현하면 더 간결하게 문제를 풀 수 있다. 

# 왜? line 22

n, m = list(map(int, input().split()))
data = list(map(int, input().split()))
start = 0
end = max(data) - 1

result = 0
while (start <= end):
	total = 0
	mid = (start / end) // 2
	for x in data:
		if x > mid:
			total += x - mid  # == calculate_remainde
	
	if total < m:
		end = mid - 1
	else:  # total == m 이더라도~ -> 재귀라면 total == m이거나 total > m이지만 calculate_remainder(m + 1) < m일때..처럼 반드시 return 조건을 만들어주어한다. 
		result = mid  # result 갱신
		start = mid + 1

print(result)