def search(nums: list[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid 

    return left if nums[left] == target else -1

print(search([-1, 2, 3, 4], 2))
print(search([1, 2, 3, 4], 5))
print(search([], 0))