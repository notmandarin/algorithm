import math

def solution(brown, yellow):
    all = brown + yellow
    
    for i in range(1,int(math.sqrt(all))+1) :
        if all % i == 0 :
            if i*2 + (all//i)*2 -4 == brown :
                return [all//i, i]
                break