# top-down: 재귀로 다이나믹 프로그래밍(메모이제이션; 캐싱)
# bottom-up: 반복(임시 저장)

d1 = [0] * 100

def recursive_fibo(x):
	if x == 1 or x == 2:
		return 1
	if d1[x] != 0:
		return d1[x]
	d1[x] = recursive_fibo(x - 1) + recursive_fibo(x - 2)
	return d1[x]

d2 = [0] * 100
d2[1] = 1
d2[2] = 1

for i in range(3, 100):  # 3 ~ 99
	d2[i] = d2[i - 1] + d2[i - 2]

print(d2[99])

# 시간복잡도 차이는 없는데, 함수 스택때문에 되도록 bottom-up으로.