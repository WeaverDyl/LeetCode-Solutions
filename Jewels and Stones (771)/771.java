// Runtime: 11 ms
// Beats 73.45% of Java submissions

// O(n^2) time with O(1) space
class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        
        for (int i = 0; i < S.length(); i++) {
            for (int j = 0; j < J.length(); j++) {
                if (S.charAt(i) == J.charAt(j)) {
                    count++;
                }
            }
        }
        
        return count;
    }
}

// O(n) with (technically) O(1) space
// Runtime: 10 ms, Beats 98.18% of Java submissions

// class Solution {
//     public int numJewelsInStones(String J, String S) {
//         int[] multiplicity = new int[58];
//         int count = 0;
        
//         for (int i = 0; i < S.length(); i++) {
//             multiplicity[S.charAt(i) - 'A']++; // Add all stones
//         }
        
//         for (int i = 0; i < J.length(); i++) {
//             count += multiplicity[J.charAt(i) - 'A'];
//         }
        
//         return count;
//     }
// }