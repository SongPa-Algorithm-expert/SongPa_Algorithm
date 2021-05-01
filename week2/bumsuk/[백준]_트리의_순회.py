import sys
sys.setrecursionlimit(10 ** 6)
read = lambda: sys.stdin.readline().strip()


def findPreorder(leftIn, rightIn, leftPost, rightPost):
    # 범위 초과시 탈출
    if leftIn > rightIn or leftPost > rightPost:
        return

    # 루트 출력
    root = postOrder[rightPost]
    print(root, end=' ')

    # 탐색 범위 설정 (각 방향 별 남은 노드 수)
    left = idx[root] - leftIn
    right = rightIn - idx[root]

    # 왼쪽, 오른쪽 탐색
    findPreorder(leftIn, leftIn + left - 1, leftPost, rightPost - right - 1)
    findPreorder(leftIn + left + 1, rightIn, rightPost - right, rightPost - 1)

if __name__ == "__main__":
    n = int(read())
    inOrder = list(map(int, read().split()))
    postOrder = list(map(int, read().split()))

    idx = [0] * (n + 1)
    for i in range(n):
        idx[inOrder[i]] = i

    findPreorder(0, n - 1, 0, n - 1)
