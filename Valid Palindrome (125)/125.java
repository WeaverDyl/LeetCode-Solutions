// Runtime: 6 ms
// Beats 57.43% of Java submissions

class Solution {
    public boolean isPalindrome(String s) {
        char[] stringArr = s.toLowerCase().toCharArray();
        int beginning = 0;
        int end = stringArr.length - 1;
        
        while (beginning < end) {
            if (!Character.isLetterOrDigit(stringArr[beginning])) {
                beginning++;
            }
            else if (!Character.isLetterOrDigit(stringArr[end])) {
                end--;
            } else {
                if (stringArr[beginning] != stringArr[end]) {
                    return false;
                }
                beginning++;
                end--;   
            }
        }
        
        return true;
    }
}