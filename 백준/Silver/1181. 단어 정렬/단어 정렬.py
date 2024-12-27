N = int(input())

S = set()
for i in range(N):
    str_input = input()
    if not str_input :
        break
    S.add(str_input)

sorted_S = sorted(list(S), key = lambda x : (len(x),x))

for s in sorted_S :
    print(s)