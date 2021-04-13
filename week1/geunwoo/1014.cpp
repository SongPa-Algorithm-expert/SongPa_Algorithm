//이문제를 풀기 위한 솔루션
#include <bits/stdc++.h>
using namespace std;
int testCase, N, M;
int cache[11][1 << 10 + 1];
int bitMap[11];
int dfs(int cnt, int cur, int idx, int line, int bitcheck, vector<vector<char>> &Room)
{
    if (idx >= M || line == N)
        return 0;
    int &result = cache[line][bitcheck];
    if (result != -1)
        return result;
    for (int i = idx; i < M; i++)
    {
        int next = cur + bitMap[i];
        if (Room[line][i] != 'x' && (i == M || (bitMap[i + 1] & bitcheck) == 0) && (i == 0 || (bitMap[i - 1] & bitcheck) == 0))
        {
            result = max(result, dfs(cnt + 1, next, i + 2, line, bitcheck, Room)); //
            result = max(result, cnt + 1 + dfs(0, 0, 0, line + 1, next, Room));
        }
    }
    if(result==-1) return 0;
    else return result;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    for (int i = 0; i < 11; i++)
    {
        bitMap[i] = 1 << i;
    }
    cin >> testCase;
    while (testCase-- > 0)
    {
        cin >> N >> M;
        memset(cache, -1, sizeof(cache));
        vector<vector<char>> vec(N, vector<char>(M));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> vec[i][j];
        int result = 0;
        for (int i = 0; i < N; i++)
            result = max(result, dfs(0, 0, 0, i, 0, vec));
        cout << result << "\n";
    }
    return 0;
}