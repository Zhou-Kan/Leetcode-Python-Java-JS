def can_partition(nums: list[int]) -> bool:
    n = len(nums)
    s = sum(nums)

    dp = [[0]]