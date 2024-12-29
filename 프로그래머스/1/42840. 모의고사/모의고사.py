def solution(answers):
    pattern_1 = [1,2,3,4,5] #5
    pattern_2 = [2,1,2,3,2,4,2,5] #8
    pattern_3 = [3,3,1,1,2,2,4,4,5,5] #10
    patterns = [pattern_1, pattern_2, pattern_3]
    sum = [0,0,0]
    len_ans = len(answers)
    
    for idx, pattern in enumerate(patterns) :
        pattern = pattern*((len_ans // len(pattern)) + 1) 
        for i in range(len_ans) :
            if answers[i] == pattern[i] :
                sum[idx] += 1
    
    max_sum = max(sum)
    
    solution = []
    for i,s in enumerate(sum) :
        if max_sum == s :
            solution.append(i+1)
    
    return solution