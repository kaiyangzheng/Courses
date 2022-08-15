def naive_moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l, r = 0, len(nums)-1
    count = 0
    while (l < r):
        if nums[l] == 0:
            nums.append(0)
            l += 1
            count += 1
        elif nums[r] == 0:
            nums.append(0)
            r -= 1
            count += 1
        else:
            l += 1
    for i in range(count):
        nums.remove(0)


def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    lastNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZero] = nums[i]
            lastNonZero += 1
    i = lastNonZero
    while (i < len(nums)):
        nums[i] = 0
        i += 1
