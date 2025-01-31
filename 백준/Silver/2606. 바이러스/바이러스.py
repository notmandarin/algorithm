import sys
from collections import deque

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    count = 0  # 1번 컴퓨터 제외

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1  # 감염된 컴퓨터 개수 증가

    return count

# 입력 처리
input = sys.stdin.readline
n = int(input().strip())  # 컴퓨터 수
m = int(input().strip())  # 연결된 네트워크 수

# 그래프 초기화 (인접 리스트)
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# 방문 체크 배열
visited = [False] * (n + 1)

# BFS 탐색 시작 (1번 컴퓨터에서 출발)
infected_count = bfs(graph, visited, 1)

# 결과 출력
print(infected_count)
