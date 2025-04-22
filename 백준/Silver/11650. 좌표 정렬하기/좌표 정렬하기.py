N = int(input())
LIST = [input().split() for _ in range(N)]
LIST.sort(key=lambda x: (int(x[0]), int(x[1]))) 

for L in LIST:
    print(' '.join(L))
