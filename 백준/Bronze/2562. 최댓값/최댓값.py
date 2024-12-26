import sys

numbers = [0]
lines = sys.stdin.readlines()

for line in lines :
    numbers.append(int(line))

Max = max(numbers)
print(Max)
print(numbers.index(Max))