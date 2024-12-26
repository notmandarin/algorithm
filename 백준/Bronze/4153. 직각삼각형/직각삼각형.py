while True :
    LIST = list(map(int, input().split()))
    if LIST == [0,0,0] :
        break
    LIST.sort()
    if LIST[2]**2 == LIST[0]**2 + LIST[1]**2 :
        print('right')
    else :
        print('wrong')