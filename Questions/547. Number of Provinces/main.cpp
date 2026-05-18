#include<iostream>
using namespace std;

vector<vector<int>> g;
vector<bool> visited;
int ans;

void dfs(int idx) {
    if (visited[idx]) return;
    visited[idx] = true;
    for (int j : g[idx]) {
        if (!visited[j]) {
            dfs(j);
            ans++;
        }
    }
}

int findCircleNum(vector<vector<int>>& isConnected) {
    int n = isConnected.size();
    vector<vector<int>> g;
    visited.assign(false, n);

    for(int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (isConnected[i][j]) {
                g[i].push_back(j);
                g[j].push_back(i);
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        dfs(i);
    }
    return ans;
}