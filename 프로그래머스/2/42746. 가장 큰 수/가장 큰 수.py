from itertools import permutations

def solution(numbers):
    str_numbers = list(map(str, numbers))
    sorted_numbers = sorted(str_numbers, key = lambda x : x*3, reverse=True)
    answer = ''.join(sorted_numbers)
    if answer[0] == '0' :
        answer = '0'
    return answer