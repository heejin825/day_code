## 실습 1

#n : 사용할 수 있는 숫자의 범위(1부터 n까지)
#m : 뽑을 숫자의 개수

n, m = list(map(int, input().split()))
# 숫자를 조합해 나갈 리스트(현재 경로)
s = []

# 백트래킹을 위한 DFS 함수 정으;
def dfs():
    # 길이가 m 인 조합이 완성되었으면 출력하고 종료
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
            
dfs()

## 실습 2
import sys
result = 0 # 방문 순서 값을 누적 저장하는 전역 변수
def sol(n, x, y):
    global result
    # (x,y) 부터 시작하는 n x n 정사각형 영역에서 (r,c)를 찾는 재귀 함수
    if x == r and y == c:
        # 기저 조건 : 찾는 좌표에 도달했으면 결과 출력 후 종료
        print(int(result))
        return
    
    if not (x <=r < x +n and y <= c < y + n):
        # 현재 정사각형이 (r,c)를 포함핮; 않으면 이 영역은 건너뜀
        result += n*n  # 이 영역에 포함된 칸 수만틈 순서를 증가시킴킴
        return
    
    # 현재 정사각형을 4등분하여 재귀적으로 탐색색
    sol(n/2, x, y)
    sol(n/2, x, y+n /2)
    sol(n/2, x+n /2, y)
    sol(n/2, x+n /2, y+n /2)
# 입력 : n은 배열 크기의 지수, r과 c는 찾고자 하는 위치치
n,r,c = map(int, sys.stdin.readline().split(' '))

# 2^n 크기의 배열로 시작 ( 1<<n == 2^n)
sol(1 << n, 0, 0)    

## 실습 3 

n = int(input())  # 커피 1잔 가격 입력 (원)

# dp[i] = i원을 만들기 위한 최소 동전 개수
# 처음엔 불가능한 값으로 초기화 (큰 수)
dp = [123456789] * 100001

# 3원과 5원짜리 동전으로 정확히 만들 수 있는 기본 경우
dp[3] = 1 # 3원은 1개 동전으로 가능
dp[5] = 1 # 5원도 1개 동전으로 가능능

# 2원부터 100000원 까지 각 금액을 만들 수 있는 최소 동전 개수 계산
for i in range(2, 100001):
    # i원이 되기 위해 5원을 추가한 경우
    if i - 5 >= 0 and dp[i - 5] != 123456789:
        dp[i] = min(dp[i], dp[i -5] +1)
        
    # i원이 되기 위해 3원을 추가하는 경우
    if i -3 >= 0 and dp[i - 3] != 123456789:
        dp[i] = min(dp[i], dp[i -3] + 1)
        
# dp[n]이 여전히 초기값이라면 만들 수 없는 경우 -> -1 출력
# 그렇지 않으면 최소 동전 개수 출력력
print(-1 if dp[n] == 123456789 else dp[n])


## 실습 4

def fibo(n):
    # 피보나치 수열의 n번째 항을 반환하는 재귀 함수
    
    if n == 1:
        return 1 # 첫 번째 항은 1
    if n == 2:
        return 1 # 두 번째 항은 1
    
    # n번째 항 = (n-1)번째 항 + (n-2)번째 항
    return fibo(n -1) + fibo(n - 2)

# 사용자 입력 : 몇 번째 피보나치 수를 구할지
n = int(input())

# 결과 출력력
print(fibo(n))

# 하나더 
arr = [0] * 91
arr[1] = 1
arr[2] = 1

for i in range(3, 91) :
    arr[i] = arr[i -1] +arr[i-2]

print(arr[n])


## 실습 5

import sys
n,m,k = map(int, sys.stdin.readline().split())


arr = [[0] * 1001 for _ in range(1001)]
pSum = [[0] * 1001 for _ in range(1001)]

for i in range(1, n+1):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, m+1):
        arr[i][j] = row[j -1]
        
        pSum[i][j] = (
            pSum[i -1][j] +
            pSum[i][j-1] -
            pSum[i-1][j-1] +
            arr[i][j]
        )
        
for _ in range(k):
    a,b,c,d = map(int, sys.stdin.readline().split())
    result = (
        pSum[c][d] -
        pSum[c][b-1] -
        pSum[a-1][d] +
        pSum[a-1][b-1]
    )
    print(result)