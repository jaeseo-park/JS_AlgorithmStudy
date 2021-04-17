#프로그래머스
#https://programmers.co.kr/learn/courses/30/lessons/43163

import copy

def dfs(checklist, now_word):
    global g_target
    global min_count
    if now_word == g_target:
        min_count = min(min_count, sum(checklist))
        return

    for i in range(len(checklist)):
        now_checklist = copy.deepcopy(checklist)
        if now_checklist[i] == False:
            count = 0
            for nw in range(len(now_word)):
                if g_words[i][nw] == now_word[nw]:
                    count += 1

            if count == len(now_word) - 1:
                now_checklist[i] = True
                dfs(now_checklist, g_words[i])


def solution(begin, target, words):
    global g_target
    g_target = target
    global g_words
    g_words = words

    # 가장 짧은 변환과정
    # 50개밖에 안되니까 그냥 모든 경우의수를 해볼까?
    if not (target in words):
        return 0

    global min_count
    min_count = 1000000000
    checklist = [False for _ in range(len(words))]

    dfs(checklist, begin)
    answer = min_count
    return answer
