N = int(input())

LIST = []
for i in range(N) :
    N = list(map(int,input().split()))
    LIST.append(N)


sorted_LIST = sorted(LIST, key=lambda x :(x[0], x[1]))

for i in sorted_LIST :
    print(*i)