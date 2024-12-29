def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    h_index = 0  # 기본값으로 초기화
    for i, x in enumerate(citations):
        if i + 1 <= x:
            h_index = i + 1
        else:
            break
    return h_index
