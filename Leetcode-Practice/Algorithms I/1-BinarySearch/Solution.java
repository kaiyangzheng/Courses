package BinarySearch;

public class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (int) (right - left) / 2;
            int isTarget = nums[mid];
            if (target == isTarget) {
                return mid;
            }
            if (target > isTarget) {
                left = mid + 1;
            }
            if (target < isTarget) {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        int target = 5;
        Solution solution = new Solution();
        int result = solution.search(nums, target);
        System.out.println(result);
    }
}
