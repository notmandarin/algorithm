def solution(answers):
    l = len(answers)
    pat_1 = [1,2,3,4,5]*l
    pat_2 = [2,1,2,3,2,4,2,5]*l
    pat_3 = [3,3,1,1,2,2,4,4,5,5]*l
    
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    for a, p in zip(answers,pat_1) :
        if a == p :
            sum1 += 1

    for a, p in zip(answers,pat_2) :
        if a == p :
            sum2 += 1
            
    for a, p in zip(answers,pat_3) :
        if a == p :
            sum3 += 1
    
    top = max([sum1, sum2, sum3])
    
    answer = []
    
    if top == sum1 :
        answer.append(1)
    if top == sum2 :
        answer.append(2)
    if top == sum3 :
        answer.append(3)
    
    return answer