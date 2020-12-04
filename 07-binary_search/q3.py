# 203쪽.
# 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다. 
# 절단기의 높이는 1부터 10억까지의 정수 중 하나인데,
# 이처럼 큰 수를 보면 당연하다는 듯이 가장 먼저 이진 탐색을 떠올려야 한다. 

# Q. 이진 탐색 기법을 여기서 어떻게 도입하지? 
# A. 기본적 발상: 절단기의 최대 높이(가장 긴 가래떡 높이)에서부터 1씩 줄여나가면서 찾기
# -> 가래떡 길이가 20억까지 되는거면 가장 극단적인 케이스는 가래떡 하나 길이가 20억이고 10억의 가래떡을 원하는 경우, 
# 1씩 줄여나가면서 10억번 연산 해야 한다. [불가능]
# 따라서 절단기의 높이를 업앤다운 게임으로 맞춰야 함. 

n, m = map(int, input().split())
data = list(map(int, input().split()))

def calculate_remainder(data, mid):
	global n
	result = 0
	for i in range(n):
		if data[i] > mid:
			result += data[i] - mid
	return result

def binary_search(data, m, start, end):
	mid = (start + end) // 2
	remainder = calculate_remainder(data, mid)
	if remainder == m or (remainder > m and calculate_remainder(data, mid + 1) < m):
		return mid
	elif remainder > m:
		return binary_search(data, m, mid + 1, end)
	else:
		return binary_search(data, m, start, mid - 1)
	

start = 0
end = max(data) - 1  # m(요청 remainder) != 0이기 때문

print(binary_search(data, m, start, end))