import sys

N = int(input())

while True :
    PS = sys.stdin.readline().strip()
    if not PS :
        break
    stack = []
    for ps in PS :
        if ps == '(' :
            stack.append(ps)
        else :
            if not stack :
                stack.append(ps)
                break
            else :
                stack.pop()
    if not stack :
        print('YES')
    else : 
        print('NO')