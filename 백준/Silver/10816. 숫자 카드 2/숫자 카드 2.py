from collections import Counter

# 입력 받기
N = int(input())
list_2 = list(map(int, input().split()))
M = int(input())
list_4 = list(map(int, input().split()))

# list_2의 요소 개수를 미리 계산
count_dict = Counter(list_2)

# list_4의 각 요소에 대해 결과 찾기
answer = [count_dict[i] for i in list_4]

# 결과 출력
print(' '.join(map(str, answer)))
