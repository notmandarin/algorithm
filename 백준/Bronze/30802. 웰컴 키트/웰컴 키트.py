import math

N = int(input())
LIST = list(map(int, input().split()))
T,P = map(int, input().split())

sum_T = 0
for L in LIST :
    sum_T += math.ceil(L/T)

print(sum_T)
print(N//P)
print(N%P)