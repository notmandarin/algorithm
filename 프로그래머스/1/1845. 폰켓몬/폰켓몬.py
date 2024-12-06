def solution(nums):
    answer = 0
    set_nums = set(nums)
    l = len(set(nums))
    if len(nums)/2 > l :
        answer = l
    else : 
        answer = len(nums)/2
    return answer