//홉 크로프트 직접 구현
//1.Maximal Matching M 을 초기화
//2. Augmenting Path가 존재할때까지 작업반복 free한것찾을때까지
//3.return M
//augmenting Path:매칭안된 path
//Alternating path:프리한 것
#include <bits/stdc++.h>
using namespace std;
#define NIL 0
struct BipartiteGraph
{
    vector<vector<int>> alternating_u_path; //if 1->2,3,4
    vector<vector<int>> alternating_v_path; //if 2<-1,3,4
    int matching = 0;

    BipartiteGraph(int size_)
    {
        alternating_u_path.resize(size_ + 1);
        alternating_v_path.resize(size_ + 1);
    }
    void addEdge(int from, int to)
    {
        alternating_u_path[from].push_back(to);
        alternating_v_path[to].push_back(from);
    }
    void HopCroft()
    {
        vector<int> pairU(alternating_u_path.size()); //u가 어떤 v에 속하는지
        vector<int> pairV(alternating_v_path.size()); //v그래프
        queue<vector<int>> uque;
        for (int from = 1; from < alternating_u_path.size(); from++)
        {
            vector<int> cur = alternating_u_path[from];
            int before_maching = matching;
            for (int to : cur)
            {
                if (pairV[to] == NIL)
                {
                    pairV[to] = from;
                    pairU[from] = to;
                    matching++;
                    break;
                }
            }
            if (before_maching == matching)
            {
                uque.push(vector<int>(1, from));
            }
            while (!uque.empty())
            {
                queue<vector<int>> vque;
                while (!uque.empty())
                {
                    vector<int> cur = uque.front();
                    uque.pop();
                    for (int i : alternating_u_path[cur.back()])
                    {
                        cur.push_back(i);
                        vque.push(cur);
                        cur.pop_back();
                    }
                }
            }
            //que에 처음에는  U에 해당하는 노드들 저장
            //que꺼내면서 V꺼내기
            //
        }
        cout << matching << "\n";
    }
};
int main()
{
    BipartiteGraph g(4);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 1);
    g.addEdge(3, 2);
    g.addEdge(4, 2);
    g.addEdge(4, 4);
    g.HopCroft();
    return 0;
}
