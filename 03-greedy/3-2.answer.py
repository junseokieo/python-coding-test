n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

count = (m // (k + 1)) * k
# count: 가장 큰 수가 더해지는 횟수
# {6, 6, 6, 5} 를 한 블럭으로 계산 -> k + 1개
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)

# 한번에 수식으로 구할 수 있겠다라는 생각을 한번 해봐야됨. 
# cnt나 count나...