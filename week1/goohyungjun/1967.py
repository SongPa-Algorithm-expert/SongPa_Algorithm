# 1967 <트리의 지름 구하기>

import sys
sys.setrecursionlimit(100000)

input = lambda: sys.stdin.readline()
visited = []
def dfs(G, v):
	# G : graph , v: current vertex, visit : visited vertices
	global visited
	visited.append(v)
	l = 0
	vv = v
	for next_v, next_l in G[v]:
		if next_v not in visited:
			x, ll = dfs(G, next_v)
			if l < next_l+ll:
				vv = x
				l = next_l+ll
	return vv, l

def solution():
	global visited
	n = int(input())
	G = [[] for i in range(n+1)]
	for _ in range(n-1):
		v1, v2, e = map(int, input().split())
		G[v1].append([v2, e])
		G[v2].append([v1, e])
	
	n1, _ = dfs(G, 1)
	visited = []
	_, answer = dfs(G, n1)
	print(answer)
	return

solution()