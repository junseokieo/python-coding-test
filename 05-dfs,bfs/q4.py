# 정답을 보고 이해하면서 작성하였습니다
# 최대한 지양해야 할듯합니다. dfs에 비해 bfs가 익숙하지 않아요

# 152쪽. 
# 이 문제는 BFS를 이용했을 때 매우 효과적으로 해결할 수 있다. 
# BFS는 시작 지점에서 가까운 노드부터 차례대로
# 그래프의 모든 노드를 탐색하기 때문이다. 
# -> 이게 무슨 말이냐 하면, BFS는 무조건 한 발자국씩만 가니까 
# 예를 들어 두 발자국으로 갈 수 있는 곳은 모두 체크를 하고 나서 세발자국을 잰다. 
# 게다가 갔던 곳은 또 안 가게 하면, 그 블럭에 있는 숫자는 최단거리겠죠??

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input())))

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	while queue:
		x, y = queue.popleft()
		for step in steps:
			nx = x + step[0]
			ny = y + step[1]
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			if graph[nx][ny] == 0:
				continue
			if graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1 # 거리 표시만 하고 아직 간 건 아님
				queue.append((nx, ny))
	return graph[n - 1][m - 1]

print(bfs(0, 0))