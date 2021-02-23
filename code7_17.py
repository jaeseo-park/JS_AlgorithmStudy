#피자배달거리


import sys
from collections import deque
import itertools
r = sys.stdin.readline

def dfs(board, house, pizza):
    comb_pizza = list(itertools.combinations(pizza, M))
    #print(comb_pizza)

    min_sumdis = 100000000

    for comb in comb_pizza:

        sum_dis = 0
        for home in house:
            min_now_comb = N*N
            for c in comb:
                temp = abs(c[0]-home[0]) + abs(c[1]-home[1])
                if min_now_comb > temp:
                    min_now_comb = temp

            sum_dis += min_now_comb

        if sum_dis < min_sumdis:
            min_sumdis = sum_dis

    return min_sumdis

N, M = map(int, r().split()) #N:맵사이즈, M:피자집개수
board = []
house = deque()
pizza = deque()
#0은 빈칸, 1은 집, 2는 피자집 - 모든집의 피자거리를 구해서 합치기
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(N):
        if row[j] == 1:
            house.append([i, j])
        elif row[j] == 2:
            pizza.append([i, j])
    board.append(row)

print(dfs(board, house, pizza))
