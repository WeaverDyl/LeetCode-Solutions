// Runtime: 10 ms
// Beats 76.68% of Java submissions

class Solution {
    public boolean judgeCircle(String moves) {
        int vertical = 0;
        int horizontal = 0;
        
        for (char move : moves.toCharArray()) {
            if (move == 'U') {
                vertical++;
            }
            if (move == 'D') {
                vertical--;
            }
            if (move == 'L') {
                horizontal++;
            }
            if (move == 'R') {
                horizontal--;
            }
        }
        
        return vertical == 0 && horizontal == 0;
    }
}