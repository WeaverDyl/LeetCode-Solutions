// Runtime: 0 ms
// Beats 100% of Java submissions

/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

      public class Solution extends GuessGame {
        public int guessNumber(int n) {
            int left = 0;
            int right = n;
            
            while (left <= right) {
                int middle = left + ((right - left) / 2);
                int guess = guess(middle);
                
                if (guess == 0) {
                    return middle;
                } else if (guess == 1) {
                    left = middle + 1;
                } else {
                    right = middle - 1;
                }
            }
            return -1;
        }
    }