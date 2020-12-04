n, m = map(int, input().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input())))

def dfs(x, y):
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	if graph[x][y] == 1:
		return False
	graph[x][y] = 0
	dfs(x - 1, y)  # step이 많지 않으면 일일이 불러도 되지만, while-if-recursive를 지키는게 나으면 steps로 묶는 것도 좋을듯
	dfs(x, y - 1)
	dfs(x + 1, y)
	dfs(x, y + 1)
	return True

cnt = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:  # dfs 자격있는지까지 dfs로 일원화 -> 깔끔?
			cnt += 1

print(cnt)