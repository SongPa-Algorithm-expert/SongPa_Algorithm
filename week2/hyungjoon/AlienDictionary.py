# Alien Dictionary
# https://practice.geeksforgeeks.org/problems/alien-dictionary/1

# Input: 
# N = 5, K = 4
# dict = {"baa","abcd","abca","cab","cad"}
# Output:
# 1
# Explanation:
# Here order of characters is 
# 'b', 'd', 'a', 'c' Note that words are sorted 
# and in the given language "baa" comes before 
# "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.

from collections import deque, defaultdict
class Solution:
    

    def findOrder(self, dict, N, K):
        charSet = set("".join(dict))
        deg = {c: 0 for c in charSet}
        graph = defaultdict(list)
        q = deque()
        
        for i in range(N-1):
            word1 = dict[i]
            word2 = dict[i+1]
            for c1, c2 in zip(word1, word2):
                if c1!=c2:
                    graph[c1].append(c2)
                    deg[c2] += 1
                    break
        
        for n, d in deg.items():
            if d == 0:
                q.append(n)
        order = ""
        while q:
            node = q.popleft()
            order += node
            for l_n in graph[node]:
                deg[l_n] -= 1
                if deg[l_n] == 0:
                    q.append(l_n)
        if set(order) != charSet:
            order = ""
        return order
        

s = Solution()
dict = ["baa", "abcd", "abca", "cab", "cad"]
dict2 =["caa","aaa","aab"]
dict3 =["ab","aa","bb"]

print(s.findOrder(dict3, 3, 2))