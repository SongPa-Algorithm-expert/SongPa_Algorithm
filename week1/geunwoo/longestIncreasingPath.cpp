#include <bits/stdc++.h>
using namespace std;
int cache[201][201];
#define Pair pair<int, int>
#define y first
#define x second
int dy[4] = {0, 0, 1, -1}, dx[4] = {
                               1,
                               -1,
                               0,
                               0,
};
class Solution
{
public:
    int longestIncreasingPath(vector<vector<int>> matrix)
    {
        memset(cache, -1, sizeof(cache));
        int result = 0;
        for (int i = 0; i < matrix.size(); i++)
            for (int j = 0; j < matrix[0].size(); j++)
                result=max(result, dfs({i, j}, matrix));
        return result;
    }
    int dfs(Pair cur, vector<vector<int>> &matrix)
    {
        int &result = cache[cur.y][cur.x];
        if (result != -1)
            return result;
        else
            result = 1;
        int cur_value = matrix[cur.y][cur.x];
        for (int i = 0; i < 4; i++)
        {
            Pair next_cur = {cur.y + dy[i], cur.x + dx[i]};
            if (next_cur.y >= 0 && next_cur.y < matrix.size() && next_cur.x >= 0 && next_cur.x < matrix[0].size())
            {
                if (matrix[next_cur.y][next_cur.x] > cur_value)
                    result = max(result, 1 + dfs(next_cur, matrix));
            }
        }
        return result;
    }
};
int main(){
    Solution *s=new Solution();
    s->longestIncreasingPath({{0},{1},{5},{5}});
}