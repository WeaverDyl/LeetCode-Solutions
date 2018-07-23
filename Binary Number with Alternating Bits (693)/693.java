// Runtime: 7 ms
// Beats 100% of Java submissions

class Solution {
    public boolean hasAlternatingBits(int n) {
        while (n != 0) {
            int prevBit = n & 1;
            n = n >> 1;
            int currBit = n & 1;
            if (prevBit == currBit) {
                return false;
            }
        }
        
        return true;
    }
}