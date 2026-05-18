def my_sqrt(x: int) -> int:
    left, right = 0, x
    while left < right:
        mid = (left + right + 1) // 2
        if mid ** 2 > x:
            right = mid - 1
        else:
            left = mid

    return left

print(my_sqrt(9))
print(my_sqrt(8))
print(my_sqrt(-1))
print(my_sqrt(0))