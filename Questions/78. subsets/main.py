def subsets(nums: list[int]) -> list[list[int]]:
    ans = []
    n = len(nums)

    def back_track(start: int, path: list[int]) -> None:
        ans.append(path[:])

        for i in range(start, n):
            path.append(nums[i])
            back_track(i + 1, path)
            path.pop()

    back_track(0, [])
    return ans