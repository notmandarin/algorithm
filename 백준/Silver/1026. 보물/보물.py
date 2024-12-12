N = int(input())  
A = list(map(int, input().split()))  
B = list(map(int, input().split()))  

A.sort(reverse=True) 
B_sorted_indices = sorted(range(N), key=lambda i: B[i])  


S = 0
for i in range(N):
    S += A[i] * B[B_sorted_indices[i]]


print(S)