#

#상어중학교
#https://www.acmicpc.net/problem/21609
#블록은 검은색 블록, 무지개 블록, 일반 블록
#검은색 블록은 -1, 무지개 블록은 0, 일반블록 1~M
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

import copy
from collections import deque

def rotate270(board):
    N = len(board)
    outputs = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            outputs[N-x-1][y] = board[y][x]
    return outputs

def gravity(board):
    N = len(board)
    outputs = copy.deepcopy(board)
    #밑에서부터 위로 검사하기
    for x in range(N):
        for y in reversed(range(N)):
            if outputs[y][x] >= 0:
                for k in range(y+1,N):#y~N-1
                    if outputs[k][x] > -2:
                        break
                    else: #-2
                        outputs[y][x],outputs[k][x] = outputs[k][x], outputs[y][x]

    return outputs

#블록그룹:연결블록집합,일반블록필수,일반블록색같음,검은X,무지개노상관
#그룹은 2이상,인접해야함,
#기준블록:무지개X,행열최소값

def check_group(board):#블록그룹체크후 삭제
    #N, M있음
    # 1.크기가 가장큰블록,무지개내림,행열내림
    max_size =0
    rainbow_size =0
    max_group =[]
    blocks = []
    for mi in range(M): #1~M
        visited = [[False for _ in range(N)] for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if board[y][x] == mi and visited[y][x] == False:
                    #큐돌려서 넣기
                    now_group = []
                    now_size = 0
                    now_rainbow = 0
                    que = deque([y,x])
                    while que:
                        now_size +=1
                        [ny,nx] = que.popleft()
                        now_group.append([ny,nx])
                        if board[ny][nx] == 0:
                            now_rainbow += 1
                        for k in range(4):
                            now_y = ny + dy[k]
                            now_x = nx + dx[k]
                            if 0<=now_y<N and 0<=now_x<N:
                                if board[now_y][now_x] == mi or board[now_y][now_x] == 0:
                                    que.append([now_y, now_x])

                    # 블록들을 리스트화하기 [크기, 무지개, 행렬, 블록주소]
                    blocks.append([now_size, now_rainbow,y,x,now_group])


    if max_size == 0:
        return False, board

    else:
        global ans
        ans += (max_size**2)
        for g in max_group:
            board[g[0]][g[1]] = -2

        return True, board


N, M = map(int, input().split())
board =[]
for i in range(N):
    board.append(list(map(int, input().split())))


#블록그룹이 있는경우 계속반복
#블록그룹없으면 종료
#1.크기가 가장큰블록,무지개내림,행열내림
#2.1번찾은거 삭제, 블록수**2점수획득
#3.중력으로 내려감,검은색고정,
#4.90도반시계회전(270)
#5.중력작용
#획득한 점수 출력
global ans
ans = 0
while True:
    ret, board = check_group(board)
    if ret == False:
        break

print(ans)
