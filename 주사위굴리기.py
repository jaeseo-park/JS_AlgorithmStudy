#백준
#https://www.acmicpc.net/problem/14499

N, M, y, x, K = map(int, input().split())
#지도의 세로 크기 N, 가로 크기 M , 주사위를 놓은 곳의 좌표 x y, 그리고 명령의 개수 K
#N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽
map_list = []

for ni in range(N):
    map_list.append(list(map(int, input().split())))

#print(map_list)

#마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
nx = [1,-1,0,0] #동서북남
ny = [0,0,-1,1] #동서북남
orders = list(map(int, input().split()))
dice = [0]* 6 #0-5, 1-4, 2-3 반대쪽인것.

for order in orders:
    #0이상이 둘다 있을땐 그대로이고, 둘중하나 0이면 서로교체됨
    if 0 <= x + nx[order-1] < M and 0<= y + ny[order-1] < N:
        changed = True
    else:
        changed = False
    if 0 <= x + nx[order-1] < M :
        x = x + nx[order-1]
    if 0<= y + ny[order-1] < N:
        y = y + ny[order-1]

    #print(y + ny[order-1], x + nx[order-1] )
    if changed == True:
        #동쪽으로 굴리면 3->1, 1->4, 4->6, 6->3, 서쪽은 반대
        #남쪽으로 굴리면 1->2, 2->6, 6->5, 5->1, 북쪽은 반대
        if order == 1:  #동쪽
            temp = dice[2]
            dice[2] = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = temp
        if order == 2:  # 서쪽
            temp = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = dice[3]
            dice[3] = temp
        if order == 3: #북
            temp = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[4]
            dice[4] = temp
        if order == 4: #남
            temp = dice[4]
            dice[4] = dice[5]
            dice[5] = dice[1]
            dice[1] = dice[0]
            dice[0] = temp

        if map_list[y][x] != 0:
            #바닥은 무조건 6임
            dice[5] = map_list[y][x]
            map_list[y][x] = 0
        else:
            map_list[y][x] = dice[5]

        #print(dice)
        print(dice[0])#윗면은 무조건 1
