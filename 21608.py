#백준 삼성기출 상어초등학교
#https://www.acmicpc.net/problem/21608
#상어 초등학교
#1.학생수 N**2, 번호달림, (r,c) 1,1부터 시작임
#2.각학생이 좋아하는 학생4명, 정해진 순서대로 자리정하기
#3.한칸에는 한명, 거리가 1인 칸을 인접칸이라함(대각선X)
#4.빈칸중에 좋아하는학생이 많은칸으로 자리정하기
#5.4번이 여러개이면 그 칸의 인접빈칸이 많은 칸으로 정함
#6.5번도 여러개면 행렬 min으로 정함
#7.모두배치후 만족도구하기 : 인접칸의 학생수,인접칸중 좋아하는 학생수로 구함
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N = int(input())
s_list = {}
inputs = []
board = [[0 for _ in range(N)] for _ in range(N)]
#print(board)
for i in range(N**2):
    tmp = list(map(int, input().split()))
    inputs.append(tmp[0])
    s_list[tmp[0]] = [tmp[1], tmp[2], tmp[3], tmp[4]]
#print(inputs)

board[1][1] = inputs[0]
#중간이 아니고 아마 1,1일것임 무조건,,, 왜냐하면 3번조건에의해서
for i in range(1, N**2):
    #1.비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
    likes = s_list[inputs[i]]
    like_list = [] #좋아하는학생개수(많),인접빈칸개수(많),y,x
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0: #빈칸,인접수리스트
                like_count= 0
                space_count =0
                for k in range(4):
                    now_y = y+dy[k]
                    now_x = x+dx[k]
                    if 0<=now_y<N and 0<=now_x<N:
                        if board[now_y][now_x] in likes:
                            like_count +=1
                        elif board[now_y][now_x] ==0:
                            space_count +=1
                like_list.append([like_count, space_count, y,x])

    like_list.sort(key = lambda x: (-x[0], -x[1],x[2],x[3]))
    # 5.4번이 여러개이면 그 칸의 인접빈칸이 많은 칸으로 정함
    # 6.5번도 여러개면 행렬 min으로 정함

    set_sit = like_list[0]
    board[set_sit[2]][set_sit[3]] = inputs[i]

#7.모두배치후 만족도구하기 : 인접칸의 학생수,인접칸중 좋아하는 학생수로 구함
ans =0
for y in range(N):
    for x in range(N):
        likes = s_list[board[y][x]]
        like_count =0
        for k in range(4):
            now_y = y + dy[k]
            now_x = x + dx[k]
            if 0 <= now_y < N and 0 <= now_x < N:
                if board[now_y][now_x] in likes:
                    like_count += 1
        if like_count == 1:
            ans +=1
        elif like_count == 2:
            ans +=10
        elif like_count == 3:
            ans +=100
        elif like_count == 4:
            ans +=1000

print(ans)
