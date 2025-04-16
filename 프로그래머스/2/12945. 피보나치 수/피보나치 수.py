import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    LIST = [0]*(n+1)
    LIST[0] = 0
    LIST[1] = 1
    for i in range(2,n+1) :
        LIST[i] = LIST[i-1] + LIST[i-2]
    return LIST[n]%1234567