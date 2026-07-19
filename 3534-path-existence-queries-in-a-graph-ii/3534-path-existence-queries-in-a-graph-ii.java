import java.util.*;

class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
     
        int[][] sorted = new int[n][2];
        for (int i = 0; i < n; i++) {
            sorted[i] = new int[]{nums[i], i};
        }
        Arrays.sort(sorted, (a, b) -> Integer.compare(a[0], b[0]));
        
        
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[sorted[i][1]] = i;
        }
        
        
        int[] nextRight = new int[n];
        int r = 0;
        for (int i = 0; i < n; i++) {
            while (r < n && sorted[r][0] - sorted[i][0] <= maxDiff) {
                r++;
            }
            nextRight[i] = r - 1;
        }
        
       
        int LOG = 18; 
        int[][] up = new int[n][LOG];
        for (int i = 0; i < n; i++) {
            up[i][0] = nextRight[i];
        }
        
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                up[i][j] = up[up[i][j-1]][j-1];
            }
        }
        
        
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int a = pos[queries[q][0]];
            int b = pos[queries[q][1]];
            
            if (a == b) {
                ans[q] = 0;
                continue;
            }
            
            
            if (a > b) {
                int temp = a;
                a = b;
                b = temp;
            }
            
            if (nextRight[a] >= b) {
                ans[q] = 1;
                continue;
            }
            
            int steps = 0;
            
            for (int j = LOG - 1; j >= 0; j--) {
                if (up[a][j] < b) {
                    a = up[a][j];
                    steps += (1 << j);
                }
            }
            
           
            if (nextRight[a] >= b) {
                ans[q] = steps + 1;
            } else {
                ans[q] = -1; 
            }
        }
        
        return ans;
    }
}