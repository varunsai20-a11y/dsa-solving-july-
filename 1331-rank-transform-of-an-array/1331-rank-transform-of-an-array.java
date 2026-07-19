import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // Step 1: Clone and sort the original array
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);
        
        // Step 2: Assign ranks to unique elements
        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int num : sortedArr) {
            if (!rankMap.containsKey(num)) {
                rankMap.put(num, rank);
                rank++;
            }
        }
        
        // Step 3: Map the ranks back to a result array
        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = rankMap.get(arr[i]);
        }
        
        return result;
    }
}