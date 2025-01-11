N = int(input())

LIST = []
for n in range(N) :
    a,b,c,d = map(int, input().split())
    LIST.append([a, b + c + d, b * c * d])

sorted_LIST = sorted(LIST, key=lambda x : (x[2],x[1],x[0]))

for i in range(3):
    print(sorted_LIST[i][0], end=' ')