def solution(n, lost, reserve):
    # 1. 모든 학생이 체육복 1개씩 있다고 가정
    students = [1] * n
    
    # 2. 도난 반영
    for l in lost:
        students[l-1] -= 1
    
    # 3. 여벌 반영
    for r in reserve:
        students[r-1] += 1
    
    # 4. 빌려주기
    for i in range(n):
        # 체육복이 없다면
        if students[i] == 0:
            # 앞 번호 학생이 여벌이 있는지 확인
            if i > 0 and students[i-1] == 2:
                students[i-1] -= 1
                students[i] = 1
            # 뒤 번호 학생이 여벌이 있는지 확인
            elif i < n-1 and students[i+1] == 2:
                students[i+1] -= 1
                students[i] = 1
                
    # 5. 체육복을 1개 이상 가진 학생의 수
    answer = sum(s >= 1 for s in students)
    return answer
