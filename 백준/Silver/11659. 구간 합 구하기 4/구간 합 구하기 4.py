import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# 누적 합 계산
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

# 구간 합 계산 및 출력
output = []
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    output.append(str(prefix_sum[j] - prefix_sum[i - 1]))

# 결과 한 번에 출력 (빠른 출력)
sys.stdout.write("\n".join(output) + "\n")
