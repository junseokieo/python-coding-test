n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R' ,'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] # L(0, -1) 이렇게 dx, dy를 계산해두는 방식! 

nx = ny = 0
for plan in plans:
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			nx = y + dy[i] # 선형대수 느낌의 사고방식.. 굳이?
	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	x, y = nx, ny

print(x, y) # print('%d %d' % (x, y)) 이렇게 안해도 돼!! python의 장점