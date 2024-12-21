N,X = map(int, input().split())
LIST = list(map(int, input().split()))

LIST = [i for i in LIST if i < X]

print(*LIST)