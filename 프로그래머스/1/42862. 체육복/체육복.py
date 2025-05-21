def solution(n, lost, reserve):
    s_lost = set(lost)
    s_reserve = set(reserve)
    
    real_lost = list(s_lost - s_reserve)
    real_reserve = list(s_reserve - s_lost)
    
    len_lost = len(real_lost)
    
    save = 0
    for l in real_lost :
        if l-1 in real_reserve :
            save += 1
            real_reserve.remove(l-1)
        elif l+1 in real_reserve :
            save += 1 
            real_reserve.remove(l+1)
    return n - len_lost + save