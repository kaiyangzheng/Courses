def naive_sortedSquares(nums: list[int]) -> list[int]:
    nums = [i**2 for i in nums]
    return sorted(nums)


def sortedSquares(nums: list[int]) -> list[int]:
    l = 0
    r = len(nums)-1
    answer = []
    while (l <= r):
        left, right = abs(nums[l]), abs(nums[r])
        if (left > right):
            answer.insert(0, left**2)
            l += 1
        else:
            answer.insert(0, right**2)
            r -= 1
    return answer
