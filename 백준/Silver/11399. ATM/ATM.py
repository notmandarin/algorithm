import sys

# 입력 받기
N = int(sys.stdin.readline())  # 사람의 수
P = list(map(int, sys.stdin.readline().split()))  # 인출 시간 리스트

# 오름차순 정렬
P.sort()

# 누적 합 계산
total_time = 0  # 최종 결과값
waiting_time = 0  # 현재까지의 대기 시간

for time in P:
    waiting_time += time  # 현재 사람의 대기 시간 누적
    total_time += waiting_time  # 누적 대기 시간 추가

# 결과 출력
print(total_time)
