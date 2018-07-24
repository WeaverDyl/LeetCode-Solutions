// Runtime: 6 ms
// Beats 99.13% of Java submissions

class Solution {
    public int findComplement(int num) {
        int res = setBits(num);
        
        return res ^ num;
    }
    
    public static int setBits(int num) {
        int res = 0;
        
        while (num != 0) {
            res = (res << 1) | 1;
            num = num >> 1;
        }
        
        return res;
    }
}