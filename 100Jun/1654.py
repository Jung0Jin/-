# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan) # 이분 탐색 처음과 끝

while start <= end: # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 # 중간 위치
    lines = 0 # 랜선 수
    for i in lan:
        lines += i // mid # 분할된 랜선 수
        
    if lines >= n: # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1

print(end)