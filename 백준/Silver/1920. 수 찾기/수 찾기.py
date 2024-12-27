N = int(input())
list_N = set(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

for m in list_M :
    if m in list_N :
        print('1')
    else :
        print('0')