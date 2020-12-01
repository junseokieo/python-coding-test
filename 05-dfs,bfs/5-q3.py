steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input())))  # TIP! map(int, input()) 으로만 하면 띄어쓰기 없이 들어오는 입력을 나누는듯

def make_ice(graph, i, j):
	graph[i][j] = 1
	for step in steps:
		ni = i + step[0]
		nj = j + step[1]
		if ni < 0 or nj < 0 or ni >= n or nj >= m:
			continue
		if graph[ni][nj] == 0:
			make_ice(graph, ni, nj)

# def dfs(graph, v, visited):
# 	visited[v] = True
# 	print(v, end=' ')
# 	for i in graph[v]:
# 		if not visited[i]:  # while + if (recursive) = backtraking
# 			dfs(graph, i, visited)

cnt = 0
for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			make_ice(graph, i, j)
			cnt += 1

print(cnt)
