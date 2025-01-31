import sys

# 입력 처리
input = sys.stdin.readline
N = int(input().strip())  # PN의 N 값
M = int(input().strip())  # 문자열 길이
S = input().strip()       # 주어진 문자열

# 결과값 (PN이 몇 번 포함되는지)
count = 0
i = 0  # 문자열 탐색 인덱스
pattern_count = 0  # 연속된 "IOI" 패턴 개수

while i < M - 1:
    if S[i:i+3] == "IOI":  # "IOI" 패턴 찾기
        pattern_count += 1  # "IOI" 패턴 개수 증가
        if pattern_count >= N:  # N개 이상 연속되면 PN 포함
            count += 1
        i += 2  # "IOI" 패턴을 찾았으면 다음 'I'에서 다시 탐색
    else:
        pattern_count = 0  # 패턴이 끊기면 초기화
        i += 1  # 다음 문자 탐색

# 결과 출력
print(count)
