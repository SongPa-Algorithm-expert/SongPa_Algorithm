"""
    - 시간 복잡도
        o(E) + o(ElogE)

        E : 간선
        다익스트라는 모든 간선을 검사하고, 모든 간선이 한번에 우선순위 큐에 들어갈 수 있다.
        그리고 그 간선들이 넣고 빼는 시간은 ElogE

    - 간략한 설명
        문제에서 루트 노드는 1이라 명시되어 있으므로, 1부터
        모든 노드들 사이의 거리를 다익스르라 알고리즘으로 파악
        그 후, 루트와 제일 거리가 먼 노드(이하 tmp)를 기준으로 한번 더 다익스트라
        알고리즘을 돌려 tmp와 거리가 먼 노드의 합을 구해 답을 구한다.
"""
from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().strip()
inf = int(1e9)


# 다익스트라 알고리즘으로 start 부터 시작해 다른 점들의 최단 거리 구하기
def dijkstra(start):
    distance = [inf for _ in range(n + 1)]
    distance[start], heap = 0, []
    heappush(heap, [start, 0])
    while heap:
        point, dist = heappop(heap)
        for nxt_point, nxt_dist in graph[point]:
            nxt_distance = nxt_dist + dist
            if distance[nxt_point] > nxt_distance:
                distance[nxt_point] = nxt_distance
                heappush(heap, [nxt_point, nxt_distance])
    return distance


if __name__ == "__main__":
    n = int(read())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, read().split())
        # 양방향 설정하기
        graph[a].append([b, c])
        graph[b].append([a, c])
    # 1부터 다른 점들의 최단 경로를 구함
    distance = dijkstra(1)
    # 1에서 가장 먼 점을 기준으로 한번더 다익스트라 알고리즘을 돌린다.
    # 예제는 9번점을 기준으로 한번 더 다익스트라를 돌린다.
    # 9번점 부터 거리가 먼 점까지(예제는 12번)의 거리를 출력한다.
    print(max(dijkstra(distance.index(max(distance[1:])))[1:]))