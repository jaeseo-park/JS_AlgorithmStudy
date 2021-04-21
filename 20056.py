#마법사 상어와 파이어볼
#https://www.acmicpc.net/problem/20056
import sys
from collections import deque
#1. 파이어볼 M개가 각 위치에 있다., ri, ci, mi, si, di #좌표, 질량, 속도, 방향
#2. 보드의 각 상하 / 좌우는 연결되어있음
#3. 파이어볼의 방향좌표가 정수로 주어진다.
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1,1,1, 0, -1, -1, -1]
#4. 이동명령시 처음에는 방향X속력으로 이동한다.
#5.이동끝난 후 : 같은칸에 있는 파이어볼은 합쳐지고 4개로 나눠짐
input = sys.stdin.readline
N, M, K = map(int, input().split())
fireball = deque()
for mi in range(M): #좌표입력받을때 -1 하기
    tmp = list(map(int, input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    fireball.append(tmp)

for ki in range(K):
    #이동시키기
    board = [[deque() for _ in range(N)] for _ in range(N)]
    for mi in range(len(fireball)): #모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다, 파이어볼의 개수는 M이 아닐수있음
        y = fireball[mi][0]
        x = fireball[mi][1]
        next_y = (y + (dy[fireball[mi][4]] * fireball[mi][3]))%N #보드의 각 상하 / 좌우는 연결되어있음
        next_x = (x + (dx[fireball[mi][4]] * fireball[mi][3]))%N
        fireball[mi][0] = next_y
        fireball[mi][1] = next_x
        board[next_y][next_x].append(mi)

    remove_list = []
    for i in range(N):
        for j in range(N):
            len_tmp = len(board[i][j])
            if len_tmp > 1: #2개이상의 파이어볼이있음
                mass_sum = 0
                dir_check = 0 #합쳐지는 파이어볼이 모두 홀/짝인경우를 체크하기
                speed_sum = 0
                #print(fireball)
                for now_idx in (board[i][j]): #변형한 후 기존좌표는 삭제하기
                    mass_sum += fireball[now_idx][2] #질량
                    dir_check += (fireball[now_idx][4]%2)  #방향,
                    speed_sum += fireball[now_idx][3]
                    remove_list.append(now_idx)
                if mass_sum >= 5:
                    if dir_check == 0 or dir_check == len_tmp : #모두 홀/짝인경우
                        fireball.append([i, j, int(mass_sum/5),int(speed_sum/len_tmp), 0]) #위치좌표, 질량, 속력,방향
                        fireball.append([i, j, int(mass_sum / 5),  int(speed_sum / len_tmp),2])
                        fireball.append([i, j, int(mass_sum / 5), int(speed_sum / len_tmp), 4])
                        fireball.append([i, j, int(mass_sum / 5), int(speed_sum / len_tmp), 6])
                    else:
                        fireball.append([i, j, int(mass_sum/5), int(speed_sum / len_tmp), 1])
                        fireball.append([i, j, int(mass_sum / 5), int(speed_sum / len_tmp), 3])
                        fireball.append([i, j, int(mass_sum / 5), int(speed_sum / len_tmp), 5])
                        fireball.append([i, j, int(mass_sum / 5), int(speed_sum / len_tmp), 7])
    new_fireball = deque()
    for fi in range(len(fireball)):
        if fi not in remove_list:
            new_fireball.append(fireball[fi])
    fireball = new_fireball

result = 0
for ki in range(len(fireball)):
    #print(fireball[ki])
    result += fireball[ki][2]
print(result)
