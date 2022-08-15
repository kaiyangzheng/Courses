def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    while (left <= right):
        mid = left + (right-left)//2
        isTarget = nums[mid]
        if (target == isTarget):
            return mid
        elif (target > isTarget):
            left = mid + 1
        elif (target < isTarget):
            right = mid - 1
    return -1


def test_search():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    index = search(nums, target)
    print(index)


test_search()
