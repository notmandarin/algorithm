from math import sqrt

def GCD(n):
    gcd_list = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            gcd_list.append([i, n // i])
    return gcd_list

def solution(brown, yellow):
    gcd_sum = GCD(brown+yellow)
    gcd_yellow = GCD(yellow)


    for y in gcd_yellow:
        for s in gcd_sum:
            if (y[0] +2 == s[0]) and (y[1] +2 == s[1]):
                answer = [s[1], s[0]]
                return answer
