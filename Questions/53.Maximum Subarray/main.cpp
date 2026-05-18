#include<iostream>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int minSum = 0, total = 0;
    int ans = INT_MIN;
    for (auto num : nums) {
        total += num;
        ans = max(total - minSum, ans);
        minSum = min(minSum, total);
    }
    return ans;
}