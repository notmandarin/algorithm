from itertools import permutations

n = int(input())

LIST= [str(i) for i in range(1,n+1)]

LIST.sort()

perms = [' '.join(p) for p in permutations(LIST, n)]

for perm in perms :
    print(perm)