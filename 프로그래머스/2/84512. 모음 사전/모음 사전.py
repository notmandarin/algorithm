from itertools import product

def solution(word):
    aeiou = ['A', 'E', 'I', 'O', 'U']

    dictionary = []
    for i in range(1, 6):
        dictionary.extend([''.join(p) for p in product(aeiou, repeat=i)])
    
    dictionary.sort()
    
    return dictionary.index(word) + 1
