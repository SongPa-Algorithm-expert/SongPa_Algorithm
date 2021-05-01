# 2263 <트리의 순회>

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline()

n=int(input())
inorder=list(map(int, input().split()))
postorder=list(map(int, input().split()))
root=postorder[-1]
# inorder 원소들 어딨는지 알기 쉽게 하기 위해 따로 저장
pos=[0]*(n+1)

for i in range(n):
    pos[inorder[i]]=i

def divide(instart, inend, poststart, postend):
    if instart > inend or poststart>postend:
        return
    root=postorder[postend]
    print(root, end=' ')
    root_inorder=pos[root]
    left=root_inorder-instart

    divide(instart, root_inorder-1, poststart, poststart+left-1)
    divide(root_inorder+1, inend, poststart+left, postend-1)
    return

divide(0,n-1,0,n-1)