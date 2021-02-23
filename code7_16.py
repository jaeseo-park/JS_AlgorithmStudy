#

import sys
from collections import deque
r = sys.stdin.readline

def dfs(board):
    for i in range(N):
        now_x = i

        if board[0][i] == 1: #사다리가 있는경우
            root = deque()
            for j in range(1, N): # 2,....9 - y축값임
                if now_x == 0:
                    if board[j][now_x] == 1 and board[j][now_x+1] == 0:
                        root.append([j,now_x])
                    elif board[j][now_x] == 1 and board[j][now_x+1] == 1: #오른쪽방향
                        root.append([j, now_x])
                        now_x += 1
                        root.append([j, now_x])
                        while(True):
                            now_x+=1
                            root.append([j, now_x])
                            if board[j+1][now_x] >= 1: break

                elif now_x == N-1:
                    if board[j][now_x] == 1 and board[j][now_x-1] == 0:
                        root.append([j,now_x])

                    elif board[j][now_x] == 1 and board[j][now_x-1] == 1: #왼쪽방향
                        root.append([j, now_x])
                        now_x -= 1
                        root.append([j, now_x])
                        while (True):
                            now_x -= 1
                            root.append([j, now_x])
                            if board[j + 1][now_x] >= 1: break

                else:
                    if board[j][now_x] == 1 and board[j][now_x+1] == 0 and board[j][now_x-1] == 0:
                        root.append([j,now_x])

                    elif board[j][now_x] == 1 and board[j][now_x+1] == 1: #오른쪽방향
                        root.append([j, now_x])
                        now_x+=1
                        root.append([j, now_x])
                        while(True):
                            now_x+=1
                            root.append([j, now_x])
                            if board[j+1][now_x] >= 1: break

                    elif board[j][now_x] == 1 and board[j][now_x-1] == 1: #왼쪽방향
                        root.append([j, now_x])
                        now_x -= 1
                        root.append([j, now_x])
                        while (True):
                            now_x -= 1
                            root.append([j, now_x])
                            if board[j + 1][now_x] >= 1: break


                if j == 9 and board[j][now_x] == 2:
                    return i
                #if j == 9:
                #    print("i:", i, "root:", root, "re:", board[j][now_x])

N = 10
board, sadari = [], deque()
goal = [0,0]

for i in range(N):
    row = list(map(int, r().split()))
    for j in range(N):
        if row[j] == 1:
            sadari.append([i, j])
        elif i == N-1 and row[j] == 2:
            goal[0] = i
            goal[1] = j
    board.append(row)

#for j in range(N):
#    print(box[j])

print(dfs(board))
