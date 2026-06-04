def trap(height: list[int]) -> int:
    ans = 0
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = height[0], height[-1]
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            ans += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            ans += right_max - height[right]
            right -= 1
    return ans

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap([4, 2, 0, 3, 2, 5]))
