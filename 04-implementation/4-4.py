n, m = list(map(int, input().split()))  # n * m 이라고 하면 무조건 n행 m열 array[n-1][m-1] 까지 존재하는 걸 의미한다!!!
x, y, direction = list(map(int, input().split()))  # x, y도 이 기준으로 생각한다. 고등학교 x,y축과는 다름에 주의!

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

game_map = []
for _ in range(n):
	game_map.append(list(map(int, input().split())))  # 2차원 배열 받는법

#  북쪽, 동쪽, 남쪽, 서쪽을 0, 1, 2, 3으로 잡아준건
#  dx = [북x, 동x, 남x, 서x], dy = [북y, 동y, 남y, 서y]로 하라고 떠먹여준 것.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1

def turn_left():
	global direction  # 방향은 이동하더라도 유지니까 전역변수
	direction -= 1
	if direction == -1:
		direction = 3

turn_cnt = 0
while True:
	turn_left()  # 왼쪽을 보고 가능하면 돌고 가는 것 == 돌고 정면이 가능하면 가는 것
	nx = x + dx[direction]
	ny = y + dy[direction]
	if visited[nx][ny] == 1 or game_map[nx][ny] == 1:
		turn_cnt += 1
		if turn_cnt == 4:
			nx = x - dx[direction]
			ny = y - dy[direction]
			if game_map[nx][ny] == 1:
				break
			else:
				x = nx
				y = ny
				turn_cnt = 0
		continue
	x = nx
	y = ny
	visited[x][y] = 1
	cnt += 1
	turn_cnt = 0

print(cnt)

# 해설을 보면서 작성하였습니다
