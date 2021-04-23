#백준 감시피하기
#https://www.acmicpc.net/problem/18428

#선생님, 학생, 장애물 위치함, 복도로 빠져나오면 선생님의 감시에 들키지않아야함
#3개의 장애물을 설치해서 모든학생들을 감시로부터 피할 수있는지 yes no, 출력
import copy

dy = [0, 0, -1, 1]
dx = [1,-1, 0, 0]
def check(board, students, teachers, comb):
    now_board = copy.deepcopy(board)
    #현재보드에서 T에게 닿은 S는 모두삭제한 후 S의 남은개수를세기
    for i in range(3):
        now_board[comb[i][0]][comb[i][1]] = 'O'

    for t in teachers:
        #4방향으로 끝까지 확인하도록 돌리기
        ty = t[0]
        tx = t[1]
        for k in range(4):
            for j in range(1, N):
                now_x = tx + (dx[k]*j)
                now_y = ty + (dy[k]*j)
                #print(now_y, now_x)
                if now_x < 0 or now_x >=N or now_y <0 or now_y >= N :
                    break #범위벗어나면
                elif now_board[now_y][now_x] == 'O': #벽에닿으면
                    break
                elif now_board[now_y][now_x] == 'S': #학생이면
                    now_board[now_y][now_x] = 'X' #삭제
    #print("--")
    #for i in range(N):
    #    print(now_board[i])
    # 벽으로막아서 모두가 살아남으면 YES
    count = 0
    for i in range(N):
        for j in range(N):
            if now_board[i][j] == 'S':
                count += 1
    if count == len(students):
        return True
    else:
        return False #한명이라도 들키는경우

import itertools
N = int(input())
board = []
students = []
teachers =[]
boxes =[]
for ni in range(N):
    board.append(list(input().split()))
    #학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X, 장애물이 존재하는 칸은 O
    for j in range(N):
        if board[ni][j] == 'S':
            students.append([ni, j])
        elif board[ni][j] == 'T':
            teachers.append([ni, j])
        elif board[ni][j] == 'X':
            boxes.append([ni, j])

#애초에 학생이나선생이 없으면 YES
if len(students) == 0 or len(teachers)== 0:
    print("YES")

else:
    combs = itertools.combinations(boxes, 3)
    combs = list(combs)
    ret = False
    for comb in combs:
        if check(board, students, teachers, comb) == True:
            ret = True
            break
    if ret == True:
        print("YES")
    else:
        print("NO")

