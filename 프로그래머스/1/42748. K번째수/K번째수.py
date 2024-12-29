def solution(array, commands):
    answer = []
    for command in commands :
        i,j,k = command[0:3] 
        slice_array = sorted(array[i-1:j])
        answer.append(slice_array[k-1])
    return answer

