// Runtime: 4 ms
// Beats 89.89% of Java submissions
class Solution {
    public int majorityElement(int[] nums) {
        Random rand = new Random();
        
        while (true) {
            int randInt = nums[rand.nextInt(nums.length)];
            
            if (countElements(randInt, nums) > (nums.length / 2)) {
                return randInt;
            }
        }
    }
    
    public static int countElements(int number, int[] list) {
        int count = 0;
        
        for (int i = 0; i < list.length; i++) {
            if (list[i] == number) {
                count++;
            }
        }
        
        return count;
    }
}