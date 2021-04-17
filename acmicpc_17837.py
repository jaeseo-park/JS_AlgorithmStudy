#백준 새로운게임2
#https://www.acmicpc.net/problem/17837

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
board = []
mal = []
chess = [[[] for _ in range(N+2)] for _ in range(N+2)]
#보드의 테두리를 파란색으로 만들기
board.append([2 for _ in range(N+2)])
for ni in range(N):
    board.append([2] + list(map(int, input().split())) + [2])
    #0은 흰색, 1은 빨간색, 2는 파란색이다.
board.append([2 for _ in range(N + 2)])
for ki in range(K):
    temp = list(map(int, input().split()))# 행, 열의 번호, 이동 방향(1~4)
    temp[2] -= 1
    mal.append(temp)
    chess[mal[ki][0]][mal[ki][1]].append(ki) #말의번호 입력
#print("mal :", mal)
#print("chess:", chess)
#이동방향 : 오,왼, 위, 아래
dx = [1, -1, 0, 0]
dy = [0,0, -1, 1]
turn = 0
break_point = False
while True:
    turn += 1
    if turn > 1000:
        break

    for ki in range(K):
        nowx , nowy = mal[ki][1], mal[ki][0]
        dir = mal[ki][2]
        nexty = nowy + dy[dir]
        nextx = nowx + dx[dir]

        # 현재 말의 스택인덱스(쌓인위치) 구하기
        stack_idx = chess[nowy][nowx].index(ki)
        next_color = board[nexty][nextx]
        if next_color == 2: #파란색인경우
            nexty = nowy - dy[dir]
            nextx = nowx - dx[dir]  #방향반대로
            if mal[ki][2] == 0:  mal[ki][2] =1
            elif mal[ki][2] == 1:  mal[ki][2] =0
            elif mal[ki][2] == 3:  mal[ki][2] =2
            elif mal[ki][2] == 2:  mal[ki][2] =3
            if board[nexty][nextx] == 2: #반대도 파란색이면 가만히
                continue

            next_color = board[nexty][nextx]
            #이동하는칸이 빨간색일수도 있음. -> 빨간색이면 변경필요함!!!!!(여기 틀렸었음)
            if next_color == 0:
                chess[nexty][nextx].extend(chess[nowy][nowx][stack_idx:])

            elif next_color == 1:  # 빨간색
                chess[nexty][nextx].extend(reversed(chess[nowy][nowx][stack_idx:]))

        elif next_color == 0:
            #chess[nexty][nextx] 값에 따라서 mal 정보 갱신
            chess[nexty][nextx].extend(chess[nowy][nowx][stack_idx:])

        elif next_color == 1: #빨간색
            chess[nexty][nextx].extend(reversed(chess[nowy][nowx][stack_idx:]))

        del (chess[nowy][nowx][stack_idx:])
        if len(chess[nexty][nextx]) >=4 :
            break_point = True
            break #4개이상 턴종료
        for now_mal in chess[nexty][nextx]:
            mal[now_mal][1], mal[now_mal][0] = nextx, nexty

    if break_point == True:
        break
if turn > 1000:
    print(-1)
else:
    print(turn)
