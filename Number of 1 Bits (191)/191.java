// Runtime: 1 ms
// Beats 98.55% of Java submissions

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;

        while (n != 0) {
            count++;
            n &= (n - 1);
        }
        
        return count;
    }
}