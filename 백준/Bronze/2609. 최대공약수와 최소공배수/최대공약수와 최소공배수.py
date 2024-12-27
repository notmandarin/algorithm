import math

A,B = map(int, input().split())


def get_division(n) :
    s = set()
    for i in range(1,int(math.sqrt(n))+1) :
        if n % i == 0 :
            s.add(i)
            s.add(n//i)
    return s

def get_GCD(a,b) :
    set_a = get_division(a)
    set_b = get_division(b)
    return(max(set_a&set_b))

def get_LCM(a,b) :
    return(int(a*b/get_GCD(a,b)))

print(get_GCD(A,B))
print(get_LCM(A,B))