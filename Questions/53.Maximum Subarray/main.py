def max_subarray(nums: list[int]) -> int:
    min_sum = 0
    total = 0
    ans = float('-inf')

    for num in nums:
        total += num
        ans = max(ans, total - min_sum)
        min_sum = min(min_sum, total)

    return ans

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))