#
x = input().split()
m = map(int, x)
a, b = m

print(x)
print(m)
print(a, b)

#
n = int(input())
data = list(map(int, input().split()))

print(n)
print(data)

#
import sys

data2 = sys.stdin.readline().rstrip() # rstrip은 '\n' 삭제
print(data2)