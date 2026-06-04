#include<iostream>
#include<unordered_set>

std::vector<int> remainingMethods(int n, int k, std::vector<std::vector<int>>& invocations) {
    std::vector<std::vector<int>> g(n);

    for (const auto& x : invocations) {
        g[x[0]].push_back(x[1]);
    }

    std::vector<bool> vis(false, n);

    std::function<void(int)> dfs = [&](int i) {
        vis[i] = true;
        for (int j : g[i]) {
            if(!vis[j]) dfs(j);
        }
    };
    dfs(k);

    std::unordered_set<int> suspicious;
    for (int i = 0; i < n; i++) {
        if (vis[i]) suspicious.insert(i);
    }

    for (const auto& edge : invocations) {
        int u = edge[0];
        int v = edge[1];

        if (!vis[u] && vis[v]) {
            std::vector<int> all_methods(n);
            for (int i = 0; i < n; i++) all_methods.push_back(i);
            return all_methods;
        }
    }

    std::vector<int> ans;
    for(int i = 0; i < n; i++) {
        if (!vis[i]) ans.push_back(i);
    }
    return ans;
};