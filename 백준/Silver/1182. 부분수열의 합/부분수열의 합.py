N,S = map(int,input().split())
L = list(map(int,input().split()))

from itertools import combinations

result = 0

for i in range(1,N+1) :
    for j in combinations(L,i) :
        if sum(j) == S :
            result += 1

print(result)