def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    row = len(park)
    column = len(park[0])
    for mat_size in mats:
        pattern = ["-1"] * mat_size
        for i in range(row - mat_size + 1):  
            for j in range(column - mat_size + 1):  
                if all(
                    park[x][j:j + mat_size] == pattern
                    for x in range(i, i + mat_size)
                ):
                    return mat_size 
    return answer