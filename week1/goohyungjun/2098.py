# 2098 Travelling Salesman Problem
import numpy as np
import sys
from itertools import combinations

input = lambda : sys.stdin.readline()

def solution(G):

	n = len(G)
	C = [[sys.maxsize for _ in range(n)] for __ in range(1<<n)]
	C[1<<0][0] = 0

	for size in range(1,n):
		for s in combinations(range(1, n), size):
			s = (0,) + s
			k = sum([1 << i for i in s]) # subset => bits
			for i in s:
				if i == 0:
					continue
				for j in s:
					if j == i:
						continue
					cur_index = k^(1<<i)
					C[k][i] = min(C[k][i], C[cur_index][j] + G[i][j])
	all_index = (1<<n) - 1
	
	return min([(C[all_index][i] + G[0][i]) for i in range(n)])

N=int(input())
G = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
	for j in range(N):
		if G[i][j] == 0:
			G[i][j] = sys.maxsize

result = solution(G)
print(result)

