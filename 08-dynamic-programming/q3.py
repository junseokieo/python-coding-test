# 정답을 참고하였습니다. 
# a_i = max(a_(i - 1), a_(i - 2) + data[i])
# 우와... 어떻게 이런 발상이 나오지

n = int(input())
data = list(map(int, input().split()))

d = [0] * 100

d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2, n):
	d[i] = max(d[i - 1], d[i - 2] + data[i])

print(d[n - 1])