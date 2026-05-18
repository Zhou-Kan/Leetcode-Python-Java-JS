#include<iostream>
using namespace std;
void backTrack(int start, int n, vector<int>& path, vector<vector<int>>& ans, vector<int>& nums) {
    ans.push_back(path);
    for (int i = 0; i < start; i++) {
        path.push_back(nums[i]);
        backTrack(i + 1, n, path, ans, nums);
        path.pop_back();
    }
}
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> ans;
    int n = nums.size();
    vector<int> path;
    backTrack(0, n, path, ans, nums);
    return ans;
}