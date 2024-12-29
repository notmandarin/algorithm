def solution(sizes): 
    width =[min(i) for i in sizes]
    height = [max(i) for i in sizes]
    return max(width)*max(height)