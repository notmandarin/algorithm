from itertools import combinations

L, C = map(int, input().split())
LIST = sorted(input().split())  # 여기! 미리 정렬

vowels = {'a', 'e', 'i', 'o', 'u'}

for comb in combinations(LIST, L):
    vowel_count = sum(1 for char in comb if char in vowels)
    consonant_count = L - vowel_count
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))
