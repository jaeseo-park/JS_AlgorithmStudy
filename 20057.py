#마법사 상어와 토네이도
#https://www.acmicpc.net/problem/20057

def rotate270(board):
    N = len(board)
    ret = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[N-j-1][i] = board[i][j]
    return ret

box = [[0, 0, 2, 0, 0],
       [0, 10, 7, 1, 0],
       [5, 0, 0, 0, 0],
       [0, 10, 7, 1, 0],
       [0, 0, 2, 0, 0]]

N = int(input())
board = []
for ni in range(N):
    board.append(list(map(int, input().split())))

set_list = []
for i in range(1, N):
    set_list.append(i)
    set_list.append(i)
set_list.append(N-1)
#print(set_list) #[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
#1. 한칸이동, 주변 9칸과 나머지 1칸에 모래 옮김
#이동하는 모래양은 소수점 아래를 버리고 남은모래는 이동하지않은 모래
#2. 이미 모래가 있을경우 모래가 더해짐
#3. 토네이도는 반시계방향으로 꺾인다.
#4. 토네이도는 [1,1,2,2,3,3,...,6,6,6]만큼 이동한다.
#5. 토네이도 이동종료후 격자밖으로 나간 모래양을 구한다.
x = int((N-1)//2)
y = int((N-1)//2)
#N은 3부터가능하기때문에 box가 다 사용되지 않을 수 있음
#왼, 아래, 오른쪽, 위쪽
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
now_dir = 0
output = 0
for sl in set_list:
    for s in range(sl):
        x = x + dx[now_dir]
        y = y + dy[now_dir]
        now_sand = board[y][x] #y의 기존모래양, y에 있는 기존모래는 삭제된다.
        after_sand = now_sand
        board[y][x] = 0
        for i in range(5):
            for j in range(5):
                if box[i][j] == 0: #박스내용물이 0이 아니어야하고 -2좌표임
                    continue
                tmp = int(now_sand * box[i][j]/100)
                if 0 <= x - 2 + j < N and 0 <= y - 2 + i < N:  # -2좌표가 보드범위내여야함
                    board[y-2+i][x-2+j] += tmp
                else:#바깥으로 나가는 모래
                    output += tmp
                after_sand -= tmp #뺄때 계산값을 고정해야되므로 변수를 별개로 계산해야됨.
        #알파구하기, 알파도 바깥이면 바깥에 더한다
        if 0 <= x + dx[now_dir]< N and 0 <= y + dy[now_dir] < N: #알파가 보드내에있는경우
            board[y + dy[now_dir]][x + dx[now_dir]] += after_sand
        else:
            output += after_sand #보드밖인경우 아웃풋에 추가

    now_dir = (now_dir+1)%4 #방향전환
    new_box = rotate270(box) #비율표 회전, 반시계로 꺾기
    box = new_box

print(output)
