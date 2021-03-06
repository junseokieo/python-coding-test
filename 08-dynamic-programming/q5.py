# 2^100 알고리즘 말고는 생각이 안나

# 226쪽. 
# 이 문제는 그리디에서 다루었던 거스름돈 문제와 거의 동일하다. 
# 단지 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점만 다르다. 
# -> 그렇기 때문에 그리디 알고리즘을 사용했던 예시처럼 매번 가장 큰 화폐 단위부터 처리하는 방법으로는 해결할 수 없다. 

# 평소 사고방식(2^n)
# 2를 넣자... 2*1 ~ 2*5000
# 3을 넣자... 어? 2*1에 3*1~3*3332 다 더할 수 있는거 아니야? -> 5000 * 3332 번
# 5을 넣자... ? 이렇게 하다보면 분명 시간초과일텐데

# 다이나믹 프로그래밍
# 1부터 끝까지 숫자 하나하나씩 기존에 있는 값으로 만들 수 있는지 확인해보자!
# 부분값 기준이 아니라 결과값 기준으로 생각하는거지(기존 분석으로 풀었던 수학문제랑 다른 방식이라 헷갈릴듯)
# k로 a_i를 만드는데 a_(i - k)가 있으면 거기에 1만 더해주면 되잖아? -> 훨씬 간단해져!!

n, m = map(int, input().split())  # 예> n = 2, m = 15

data = []
for _ in range(n):
	data.append(int(input()))  # 예> [2, 3]

d = [10001] * (m + 1)  # 나올 수 있는 결과값 최대가 10000이기 때문
d[0] = 0
for i in range(n):
	for j in range(data[i], m + 1):  # 예> data[0] = 2, data[1] = 3, m + 1 = 16. So, 2 ~ 15, 3 ~ 15
		if d[j - data[i]] != 10001:
			d[j] = min(d[j], d[j - data[i]] + 1)

if d[m] == 10001:
	print(-1)
else:
	print(d[m])

# 그런데 이건 다시 만들라고해도 못만들겠는데? 
# 진짜 어려운 문제다. 