import math
from itertools import permutations

answer = []
def solution(numbers):
    perm_list = []
    
    for r in range(1, len(numbers)+1) :
        perm = permutations(numbers, r)
        for p in perm :
            perm_list.append(''.join(p))
    
    int_list = []
    for l in perm_list :
        int_list.append(int(l))
    
    int_list = list(set(int_list))
    
    for i in int_list :
        is_Prime = True
        if i >= 2 :
            for j in range(2,int(math.sqrt(i))+1) :
                if i % j == 0 :
                    is_Prime = False
                    break
            if is_Prime == True :
                answer.append(i)
    return len(answer)