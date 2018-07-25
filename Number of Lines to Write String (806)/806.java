// Runtime: 2 ms
// Beats 88.86% of Java solutions

class Solution {
    public int[] numberOfLines(int[] widths, String S) {
        int totalWidth = 0;
        int totalLines = 1;
        
        for (char letter : S.toCharArray()) {
            int currWidth = widths[letter - 'a'];
            totalWidth += currWidth;
            
            if (totalWidth > 100) {
                totalLines++;
                totalWidth = currWidth;
            }
        }
        
        return new int[] {totalLines, totalWidth};
    }
}