import sys
from collections import deque

def process_ac(commands, array):
    is_reversed = False
    dq = deque(array)

    for command in commands:
        if command == "R":
            is_reversed = not is_reversed  # 뒤집기 상태 변경
        elif command == "D":
            if not dq:
                return "error"  # 빈 배열에서 삭제 시 에러
            if is_reversed:
                dq.pop()  # 뒤집힌 경우 뒤에서 삭제
            else:
                dq.popleft()  # 정방향인 경우 앞에서 삭제

    # 최종 결과
    if is_reversed:
        dq.reverse()  # 실제로 뒤집기
    return "[" + ",".join(map(str, dq)) + "]"

# 입력 처리
input = sys.stdin.readline
T = int(input().strip())  # 테스트 케이스 개수
results = []

for _ in range(T):
    commands = input().strip()  # 수행할 함수
    n = int(input().strip())  # 배열 크기
    arr_input = input().strip()[1:-1]  # 대괄호 제거
    array = deque(map(int, arr_input.split(","))) if arr_input else deque()  # 빈 배열 처리

    results.append(process_ac(commands, array))

# 결과 출력 (빠른 출력)
sys.stdout.write("\n".join(results) + "\n")
