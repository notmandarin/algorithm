H,M = map(int, input().split())

if M < 45 :
    H -= 1
    M = M + 60 - 45
    if M == 60 :
        H += 1 
        M = 0

else : 
    M -= 45
    
if H < 0 :
    H = 24 + H
    
print(H,M)