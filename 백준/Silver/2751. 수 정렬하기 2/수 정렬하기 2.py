import sys

numbers = sys.stdin.readlines()  # 모든 줄 읽기
numbers = [int(i.strip()) for i in numbers[1:]]
sorted_numbers = sorted(set(numbers))
for number in sorted_numbers:
    print(number)