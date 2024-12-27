while True :
    N = input()
    if N == '0' :
        break    
    N_1 = N[::-1]
    if N == N_1 :
        print('yes')
    else :
        print('no')
