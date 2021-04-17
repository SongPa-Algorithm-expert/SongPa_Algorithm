# 1014 컨닝 

import sys

input = lambda : sys.stdin.readline()

def bitcheck(i, M):
	for j in range(M-1):
		bb = 3 << j # 3 => 11 
		if i & bb == bb:
			return False
	return True

def generate_bitSet(M):
	bitSet = []
	
	for i in range(1<<M):
		if bitcheck(i, M):
			bitSet.append(i)
	return bitSet

def countbit(bits,M):
	cnt = 0
	i = 1
	for ii in range(M):
		if (i<<ii)&bits:
			cnt+=1
	return cnt

def availableCheck(j,k,M):
	# j : front row, 
	# k : behind row
	for i in range(M):
		if (1<<i)&j:
			if (1<<i+1) & k: return False
			if i > 0 and (1<<i-1)&k : return False
	return True

def seatCheck(j, arr, M):
	for ii in range(M):
		if j&(1<<ii) and arr[M-1-ii]=='x': 
			return False
	return True


def solution(arr, N, M):
	answer = 0
	d = [[0]*(1<<M) for _ in range(N)]
	bitSet = generate_bitSet(M)
	for j in bitSet:
		if seatCheck(j, arr[0], M):
			d[0][j] = countbit(j, M)
			answer = max(answer, d[0][j])
	for i in range(1, N):
		for j in bitSet: # current row cases
			if seatCheck(j, arr[i], M) == False:
				continue
			for k in bitSet: # front row cases
				if availableCheck(j,k,M):
					d[i][j] = max(d[i][j], d[i-1][k] + countbit(j,M))
					answer = max(answer, d[i][j])
	print(answer)
	return


C = int(input())
for _ in range(C):
	N, M = list(map(int, input().split()))
	arr = []
	for _ in range(N):
		s = input()
		s = s[:-1]
		aa = [c for c in s]
		arr.append(aa)
	solution(arr, N, M)