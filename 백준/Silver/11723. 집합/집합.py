import sys

S = 0  # 집합을 비트마스킹 정수로 표현
input = sys.stdin.readline  # 한 줄씩 읽어 메모리 절약

M = int(input())  # 연산 개수

for _ in range(M):
    command = input().split()
    
    if command[0] == "add":
        S |= (1 << (int(command[1]) - 1))
    
    elif command[0] == "remove":
        S &= ~(1 << (int(command[1]) - 1))
    
    elif command[0] == "check":
        print(1 if (S & (1 << (int(command[1]) - 1))) else 0)
    
    elif command[0] == "toggle":
        S ^= (1 << (int(command[1]) - 1))
    
    elif command[0] == "all":
        S = (1 << 20) - 1  # 모든 원소를 추가
    
    elif command[0] == "empty":
        S = 0  # 공집합으로 변경
