def naive_rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    shifted = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        shifted[(i+k) % len(nums)] = nums[i]
    for i in range(len(nums)):
        nums[i] = shifted[i]


def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    l, r = 0, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = 0, k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = k, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
