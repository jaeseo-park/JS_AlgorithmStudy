#마법사 상어와 파이어스톰
#https://www.acmicpc.net/problem/20058
import copy
from collections import deque

def rotate90(inputs): #시계방향 90도
    N = len(inputs)
    outputs = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            outputs[j][N-1-i] = inputs[i][j]

    return outputs

def dfs(y, x,visited, board):
    #global now_count
    now_count = 0
    visited[y][x] = True

    next= deque()
    next.append([y,x])
    while len(next) >0:
        [y, x]= next.pop()
        now_count += 1

        for i in range(4):
            if 0 > y+dy[i] or 0 > x+dx[i] or len(board) <= y+dy[i] or len(board) <= x+dx[i]:
                continue
            else:
                if board[y+dy[i]][x+dx[i]] > 0 and visited[y+dy[i]][x+dx[i]] == False :
                    #dfs(y+dy[i], x+dx[i], visited, board)
                    visited[y+dy[i]][x+dx[i]] = True
                    next.append([y+dy[i], x+dx[i]])

    global max_block
    max_block = max(max_block, now_count)

N, Q = map(int, input().split())
board = [] #얼음의 양이 주어지는 보드
for ni in range(2**N):
    board.append(list(map(int, input().split())))

magic = list(map(int, input().split())) #마법 시전 리스트
#시전할때 단계 L을 결정해야함,
#magic[] 이 L인경우 가로세로 2**L크기로 나눈다, 1이면 2*2로나눔

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for mi in magic:
    now_size = 2**mi
    #모든 부분격자를 90도로 회전
    for i in range(0, len(board)-1, now_size):
        for j in range(0, len(board)-1, now_size):
            now_block = [[0]*now_size for _ in range(now_size)]
            for k in range(now_size):
                for t in range(now_size):
                    now_block[k][t] = board[k+ i][t+ j]
            new_block = rotate90(now_block)
            for k in range(now_size):
                for t in range(now_size):
                    board[k+ i][t+ j] = new_block[k][t]

    sum = 0
    new_board = copy.deepcopy(board)
    #회전후 얼음칸에 인접하지않은 얼음칸은 얼음이 1줄어든다.
    for i in range(len(board)):
        for j in range(len(board)):
            count = 0
            for k in range(4):
                if 0 > i+dy[k] or 0 > j+dx[k] or len(board) <= i+dy[k] or len(board) <= j+dx[k]:
                    continue

                if board[i+dy[k]][j+dx[k]] > 0:
                    count += 1

            if count < 3 and new_board[i][j] >0:
                new_board[i][j] -=1
    board = new_board
#for i in range(len(board)):
#    print(board[i])
#가장 큰 덩어리가 차지하는 개수는 dfs로구할것
visited = [ [False] * len(board) for _ in range(len(board))]
global max_block
max_block = 0
for i in range(len(board)):
    for j in range(len(board)):
        sum += board[i][j] #남아있는 얼음의합
        if board[i][j] > 0 and visited[i][j] == False:
            global now_count
            now_count = 0
            dfs(i, j, visited, board)

#for i in range(len(board)):
#    print(visited[i])
print(sum) #남은얼음
print(max_block) #가장큰덩어리의 칸의 개수
