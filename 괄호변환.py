#프로그래머스
#https://programmers.co.kr/learn/courses/30/lessons/60058

def check(st): #올바른 문자열인지 확인하기
    que = []
    for t in st:
        if t == '(':
            que.append('(')
        elif t == ')':
            if len(que) == 0:
                return False
            if que[-1] == '(':
                que.pop()
            else:
                return False

    if len(que) == 0:
        return True
    else:
        return False

def sli(p): #문자열 자르는 함수
    if p == '':
        return p

    else:
        open_count = 0
        close_count =0

        for i in range(len(p)):
            if p[i] == '(':
                open_count += 1
            elif p[i] == ')':
                close_count += 1

            if open_count == close_count:
                u = p[:i+1]
                v = p[i+1:]
                if check(u) : #u가 올바르면
                    return u+sli(v)
                else: #균형인데 올바르지 않은경우
                    now_str = '('+sli(v)+ ')'
                    now_u = u[1:-1]
                    for ui in now_u:
                        if ui == '(':
                            now_str = now_str+')'
                        elif ui == ')':
                            now_str = now_str+'('
                    #print("now_str: ", now_str)
                    return now_str

def solution(p):
    answer = ''
    #균형을 올바른으로 바꾸기

    answer = sli(p)

    return answer
