# dfs는 stack, bfs는 queue를 사용한다
from collections import deque

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if not visited[i]:  # while + if (recursive) = backtraking
			dfs(graph, i, visited)

def bfs(graph, start, visited):
	queue = deque([start])  # queue에 1을 넣고 시작
	visited[start] = True
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True  # 아직 visit 하지도 않았는데 먼저 켜는 이유 : queue에 들어와있는 것만으로도 언젠가는 방문할 것이 확정이기 때문


graph = [
	[], # 0번
	[2, 3, 8], 
	[1, 7], 
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8], 
	[1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)
print('')
visited = [False] * 9
bfs(graph, 1, visited)