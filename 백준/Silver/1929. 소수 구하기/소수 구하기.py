import math

A,B = map(int, input().split())

for i in range(max(2, A), B+1) :
    for j in range(2,int(math.sqrt(i)+1)) :
        if i%j == 0 :
            break
    else :
        print(i)