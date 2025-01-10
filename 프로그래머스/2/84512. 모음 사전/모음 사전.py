def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    place_values = [781, 156, 31, 6, 1]  # 각 자리수의 기여도 미리 계산
    result = 0
    
    for i, char in enumerate(word):
        index = vowels.index(char)  # 해당 문자의 인덱스 (0 ~ 4)
        result += index * place_values[i] + 1  # 해당 자리의 기여도 계산
    
    return result