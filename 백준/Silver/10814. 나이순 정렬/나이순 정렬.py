N = int(input())

LIST = []
for _ in range(N):
    age, name = input().split()
    LIST.append((int(age), name))  # 나이와 이름만 저장

# 나이를 기준으로 정렬 (가입 순서는 유지됨)
LIST.sort(key=lambda x: x[0])

# 정렬 결과 출력
for age, name in LIST:
    print(age, name)
