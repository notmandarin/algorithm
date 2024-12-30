N = int(input())

LIST = []
for idx in range(N):
    age, name = input().split()
    LIST.append((int(age), idx, name))  # 나이, 가입 순서, 이름 저장

# 나이를 우선 기준으로 정렬, 가입 순서를 보조 기준으로 정렬
sorted_LIST = sorted(LIST, key=lambda x: (x[0], x[1]))

# 정렬 결과 출력
for age, _, name in sorted_LIST:
    print(age, name)
