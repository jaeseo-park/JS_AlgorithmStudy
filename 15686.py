#https://www.acmicpc.net/problem/15686
#15686 치킨배달
from itertools import combinations

N, M = map(int, input().split()) #M(1 ≤ M ≤ 13)
board = []
chickens =[]
houses = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 1:
            houses.append([i, j]) #y,x
        elif board[i][j] == 2:
            chickens.append([i, j]) #y,x
#M:폐업시키지 않을 치킨집의 개수
#0은 빈 칸, 1은 집, 2는 치킨집
combs = combinations(chickens, M)
ans = 100000000
for comb in combs:
    sum = 0
    for house in houses:
        now_min = 1000000
        for now_c in comb:
            dis = abs(now_c[0] - house[0]) + abs(now_c[1] - house[1])
            now_min = min(dis, now_min)
        sum += now_min
    ans = min(sum, ans)

print(ans)
