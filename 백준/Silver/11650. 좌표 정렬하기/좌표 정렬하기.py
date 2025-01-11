N = int(input())

LIST = [list(map(int,input().split())) for i in range(N)]

sorted_LIST = sorted(LIST)

for i in sorted_LIST :
    print(*i)