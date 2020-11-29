steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
#  이렇게 모든 이동가능한 수를 미리 만들어놓기!

data = input()
row = int(data[1])
col = int(ord(data[0]) - ord('a') + 1)  # ord() -> ASCII 코드 번호

cnt = 0
for step in steps:
	ncol = col + step[0]
	nrow = row + step[1]
	if ncol < 1 or nrow < 1 or ncol > 8 or nrow > 8:
		continue
	cnt += 1

print(cnt)

#  답안과 유사함.