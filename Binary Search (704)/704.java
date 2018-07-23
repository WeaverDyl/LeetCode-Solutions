// Runtime: 2 ms
// Beats 100% of Java submissions

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        while (left <= right) {
            int middle = (left + right) / 2;
            if (target > nums[middle]) {
                left = middle + 1;
            } else if (target < nums[middle]) {
                right = middle - 1;
            } else if (target == nums[middle]) {
                return middle;
            }
        }
        
        return -1;
    }
}