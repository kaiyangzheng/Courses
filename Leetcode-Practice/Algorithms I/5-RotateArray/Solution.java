class Solution {
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        
        int l = 0;
        int r = nums.length-1;
        while (l < r){
            swap(nums, l, r);
            l++;
            r--;
        }
        
        l = 0;
        r = k-1;
        while (l < r){
            swap(nums, l, r);
            l++;
            r--;
        }
        
        l = k;
        r = nums.length-1;
        while (l < r){
            swap(nums, l, r);
            l++;
            r--;
        }
        
    }
}