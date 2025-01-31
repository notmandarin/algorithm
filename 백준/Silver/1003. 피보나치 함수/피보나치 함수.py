import sys

def fibonacci_count(n):
    # DP 테이블 초기화
    zero = [0] * 41
    one = [0] * 41

    # 기본 피보나치 호출 횟수 설정
    zero[0], one[0] = 1, 0  # fibonacci(0)
    zero[1], one[1] = 0, 1  # fibonacci(1)

    # DP로 0과 1의 호출 횟수 미리 계산
    for i in range(2, 41):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]

    return zero, one

# 빠른 입력 처리
input = sys.stdin.readline
T = int(input().strip())

# 0과 1 호출 횟수 사전 계산
zero, one = fibonacci_count(40)

# 각 테스트 케이스 처리
results = []
for _ in range(T):
    N = int(input().strip())
    results.append(f"{zero[N]} {one[N]}")

# 결과 한 번에 출력 (빠른 출력)
sys.stdout.write("\n".join(results) + "\n")
