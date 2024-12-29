from itertools import permutations
from math import sqrt

def solution(numbers):
    numbers_list = list(numbers)
    len_numbers = len(numbers)
    per_numbers = [''.join(i) for p in range(1,len_numbers+1) for i in permutations(numbers_list, p)]    
    int_numbers = [int(j) for j in per_numbers]
    final_numbers = list(set(int_numbers))
    
    answer = 0
    for f in final_numbers :
        if f>=2 :
            for i in range(2,int(sqrt(f)+1)) :
                if f%i == 0:
                    break
            else :
                answer +=1
    
    return answer 