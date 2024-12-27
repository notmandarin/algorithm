from itertools import combinations

N,M = map(int, input().split())
LIST = list(map(int,input().split()))

comb = [sum(i) for i in combinations(LIST, 3)]

comb_max = [i for i in comb if i<=M]

print(max(comb_max))