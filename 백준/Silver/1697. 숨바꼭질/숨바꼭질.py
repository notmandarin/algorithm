from collections import deque

def bfs(n, k):
    if n == k:
        return 0  # 시작과 목표가 같으면 0초

    MAX = 100000
    visited = [-1] * (MAX + 1)  # 방문 여부 및 최소 시간 저장
    queue = deque([n])  # 큐 초기화
    visited[n] = 0  # 시작점 방문 표시

    while queue:
        x = queue.popleft()

        for nx in (x - 1, x + 1, 2 * x):  # 가능한 이동
            if 0 <= nx <= MAX and visited[nx] == -1:  # 범위 내 & 미방문
                visited[nx] = visited[x] + 1  # 현재 위치에서 +1초
                if nx == k:
                    return visited[nx]  # 동생 위치 도착 시 종료
                queue.append(nx)  # 다음 위치 추가

    return -1  # 도달 불가능한 경우 (이론상 발생하지 않음)

# 입력
N, K = map(int, input().split())
print(bfs(N, K))
