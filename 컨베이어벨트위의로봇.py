#백준
#https://www.acmicpc.net/problem/20055

N, K = map(int, input().split())

Alist = list(map(int, input().split())) #내구도 - 2N개만큼 입력됨
#벨트길이 :2N, 1번시작, N번 내려감, 내구도 0인게 K이상

step =0
robot = [0 for _ in range(N)]
#print(robot)
#for ni in range(N - 2, 0, -1):  # N-1, N-2 나옴 0 빼고
#    print("ni:", ni)

while(True):
    #print(Alist)
    count = 0
    for A in Alist:
        if A == 0:
            count += 1

    if count >= K:
        break

    #0~2N-2 ->입력 1~2N-1
    Alist[0], Alist[1:] = Alist[(2*N) -1], Alist[:(2*N) -1] #회전
    print(Alist)
    robot[1:] = robot[:N-1] #앞으로가는 로봇
    robot[0] = 0 #앞으로 이동해서 없음
    robot[N-1] = 0 #내리기
    print(robot)

    for ni in range(N-2, -1, -1): # N-1, N-2 나옴 0 빼고
        #print("ni:", ni)
        if Alist[ni+1] > 0 and robot[ni+1] == 0 and robot[ni] == 1:
            robot[ni+1] = robot[ni]
            robot[ni] = 0
            Alist[ni + 1] -= 1

    if robot[0] == 0 and Alist[0] > 0: #로봇올리기
        robot[0] = 1
        Alist[0] -= 1

    step +=1

print(step)


