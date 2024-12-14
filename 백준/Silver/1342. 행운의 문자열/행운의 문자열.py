from collections import Counter

# 문자열 입력
S = input().strip()

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if len(S) == len(set(S)):
    print(factorial(len(S)))
else:
    counter = Counter(S)
    
    memo = {}

    def backtrack(prev, counts):
        if sum(counts.values()) == 0:
            return 1
        
        key = (prev, tuple(sorted(counts.items())))
        if key in memo:
            return memo[key]
        
        total = 0
        for c in counts:
            if counts[c] > 0 and c != prev:
                counts[c] -= 1
                total += backtrack(c, counts)
                counts[c] += 1
        
        memo[key] = total
        return total
    
    print(backtrack('', counter))
