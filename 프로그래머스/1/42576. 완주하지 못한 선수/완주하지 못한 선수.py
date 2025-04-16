from collections import Counter

def solution(participant, completion):
    counter_p = Counter(participant)
    counter_c = Counter(completion)
    answer = counter_p - counter_c
    return list(answer.keys())[0]
