## DFS 실습 1

# 인접 리스트 방식 그래프 정의
graph = [
    [],         # 0번 노드는 사용하지 않음
    [2,3],      # 1번 노드는 2번, 3번 노드로 연결됨
    [],         # 2번 노드는 연결 없음
    [],         # 3번 노드도 연결 없음
    []          # 4번 노드는 연결 없음 (예비 공간)
    
]

visited = [False] * 5       # 방문 여부 저장 배열
access_count = 0            # 실제로 접근한 횟수를 세는 변수

def dfs_list(now):
    global access_count
    visited[now] = True         # 현재 노드 방문 표시   
    print(now, end= ' ')        # 현재 노드 출력
    
    for next_node in graph[now]:        # 연결된 노드만 순회
        access_count += 1               # 연결된 노드에 접근하므로 접근 횟수 증가
        if not visited[next_node]:      # 아직 방문하지 않은 노드라면
            dfs_list(next_node)         # DFS 재귀 호출
            
dfs_list(1)         # 1번 노드에서 DSF
print("\n접근 횟수 (리스트):", access_count)

## DFS 실습 2

# 인접 행렬 방식 그래프 정의(4 x 4)
graph = [
    [0, 0, 0, 0, 0],        # 0번 노드 미사용
    [0, 0, 1, 1, 0],        # 1번 노드 2번과 3번과 연결
    [0, 0, 0, 0, 0],        # 2번 노드 연결 없음
    [0, 0, 0, 0, 0],        # 3번 노드 연결 없음
    [0, 0, 0, 0, 0]         # 4번 노드 연결 없음
]

visited = [False] * 5       # 방문 여부 저장 배열
access_count = 0            # 실제로 접근한 횟수를 세는 변수

def dfs_matrix(now):
    global access_count
    visited[now] = True         # 현재 노드 방문 표시   
    print(now, end= ' ')        # 현재 노드 출력
    
    for next_node in range(1, 5):       # 1 ~ 4번 노드까지 모두 확인인
        access_count += 1               # 무조건 접근 (0이든 1이든든)
        if graph[now][next_node] == 1 and not visited[next_node]:
            dfs_matrix(next_node)       # 연결되어 있고 아직 방문 안 한 노드 제거거
            
dfs_list(1)         # 1번 노드에서 DSF 시작작
print("\n접근 횟수 (행렬):", access_count)


## BFS 실습

from collections import deque

graph = [
    [],           # 0번 노드는 사용하지 않음
    [2,3],        # 1번 노드는 2번, 3번 노드로 연결됨
    [1],          # 2번 노드는 1 연결 
    [1, 4, 5],    # 3번 노드도 1, 4, 5연결 
    [3],          # 4번 노드는 3 연결 
    [3]           # 5번 노드는 3 연결결
]

visited = [False] * 6               # 방문 여부 저장 (노드 1~5)

def bfs(start):
    queue = deque()                 # 큐 선정
    queue.append(start)             # 시작 노드를 큐에 삽입
    visited[start] = True           # 시작 노드 방문 표시
    
    while queue:
        now = queue.popleft()       # 큐에서 가장 앞 노드 꺼냄
        print(now, end=' ')         # 현재 노드 출력
        
        # 현재 노드와 연결된 모든 노드 확인
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True       # 방문 표시
                queue.apprnd(next_node)         # 큐에 삽입
                
# 실행행
bfs(1)
