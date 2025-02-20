def solution(name):
    # 1) 상하(▲/▼) 이동 비용: 각 문자별로 'A'에서 목표 문자로 바꾸는 데 필요한 최소 조작 수
    def up_down_cost(ch):
        # 예: ch = 'J' (ASCII 74), 'A' (ASCII 65)
        forward = ord(ch) - ord('A')            # 위(▲)로 이동
        backward = 26 - forward                 # 아래(▼)로 이동
        return min(forward, backward)
    
    n = len(name)
    
    # 모든 문자에 대해 'A'에서 해당 문자로 바꾸는 상하 이동 횟수 합
    vertical_moves = sum(up_down_cost(ch) for ch in name)
    
    # 2) 가로(좌/우) 이동 최소화
    #    - 먼저 "단순히 오른쪽으로 끝까지 이동하는" 경우를 기본값으로 둔다 (커서 이동 횟수 = n - 1)
    horizontal_moves = n - 1
    
    # i = 0부터 n-1까지 탐색하면서,
    # "i 뒤쪽에 연속된 'A'가 얼마나 있는지" 확인 후 그에 따라 최적 경로를 갱신
    for i in range(n):
        # 다음 인덱스 next_i를 찾아서,
        # 그 뒤로 연속된 'A' 영역을 지나 어디까지 건너뛸 수 있는지 확인
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        # case 1) 오른쪽으로 i까지 이동한 뒤, 다시 왼쪽으로 돌아가는 경우
        #   커서 이동 횟수: i (오른쪽 이동) + (n - next_i) (왼쪽으로 이동)
        #   여기서 "2*i + (n - next_i)" 혹은 "i + 2*(n - next_i)" 형태 등
        #   원형 이동이므로 왼쪽/오른쪽으로 돌아가는 두 가지를 비교해야 함
        
        # 1) 오른쪽으로 i번 → 왼쪽으로 (n - next_i)번
        #    총 이동: i + (n - next_i) + (추가로 되돌아가기 위한 i만큼 더 갈 수도 있으나,
        #    사실상 '원형'이라 2가지 공식 중 더 작은 쪽을 택해주면 된다)
        
        # 실제로 널리 사용되는 공식 두 가지를 모두 적용 후 최솟값을 취하는 경우가 많다:
        #   - 이동 횟수 A = 2*i + (n - next_i)
        #   - 이동 횟수 B = i + 2*(n - next_i)
        # 둘 다 "오른쪽 → 왼쪽" 혹은 "왼쪽 → 오른쪽" 으로 돌아갈 때의 거리
    
        move_case_1 = 2 * i + (n - next_i)      # 오른쪽으로 i번 갔다가, 왼쪽으로 돌아가는 경우
        move_case_2 = i + 2 * (n - next_i)      # 오른쪽 조금 + 왼쪽 크게 돌아가는 경우 (또는 반대)
        
        # 기존 horizontal_moves와 비교하여 최솟값 갱신
        horizontal_moves = min(horizontal_moves, move_case_1, move_case_2)
    
    # 최종적으로, 모든 문자에 대한 상하 이동 횟수 + 최소 가로 이동 횟수
    return vertical_moves + horizontal_moves
