from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    dp = deque()
    ans = []
    right = 0

    for right in range(n):
        while dp and nums[dp[-1]] <= nums[right]:
            dp.pop()
        dp.append(right)

        if dp[0] <= right - k:
            dp.popleft()
        
        if right >= k - 1:
            ans.append(nums[dp[0]])
        
        right += 1
    
    return ans

print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(max_sliding_window([1], 1))
# O(n), O(k)

# I'll use a monotonic decreasing deque of indices, where the front is always
# the index of the current window's maximum
# As I loop through nums, for each new element:
# 1. I need to check if the new element is larger than the top one. If it is, I pop the 
# back one out first.
# 2. Add the current index to the back of the deque
# 3. I also need to check if the size of the window exceeds the limit.
