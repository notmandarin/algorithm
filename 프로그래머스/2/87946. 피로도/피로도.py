from itertools import permutations

def solution(k, dungeons):
    max_dg = 0

    for permutation in permutations(dungeons):
        current_hp = k
        current_dg = 0

        for i in permutation:  # permutation=[[80,20],[50,40],[30,10]]
            if current_hp >= i[0]:  
                current_hp -= i[1]  
                current_dg += 1     
            else:
                break

        max_dg = max(max_dg, current_dg)
    return max_dg
