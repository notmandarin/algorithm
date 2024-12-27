import math

N = int(input())
LIST = list(map(int, input().split()))

sum = 0

for L in LIST : # L = 9
    if L != 1 :
        for i in range(2,round(math.sqrt(L))+1) :  # 2 3
            if L%i == 0 :
                break
        else :
            sum+=1
        
print(sum)