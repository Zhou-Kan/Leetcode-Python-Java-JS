def max_area(height: list[int]) -> int:
    n = len(height)
    left, right = 0, n - 1
    ans = 0

    while left < right:
        ans = max(ans, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans 

print(max_area([1, 1]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

