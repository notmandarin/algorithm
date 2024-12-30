from itertools import combinations

while True :
    LIST = list(map(int,input().split()))
    if LIST == [0] :
        break
    
    N = LIST[0]
    TEST = LIST[1:]
    
    ans = []
    for i in combinations(TEST, 6) :
        for j in i :
            print(j, end=' ')
        print()
    print()