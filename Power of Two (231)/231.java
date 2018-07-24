// Runtime: 1 ms
// Beats 100% of Java submissions

class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & n - 1) == 0;
    }
}