import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        // Step 1: Build the adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];
        int completeComponentsCount = 0;

        // Step 2: Iterate through all vertices to find connected components
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int[] counts = new int[2]; // counts[0] = vertex count, counts[1] = edge count
                dfs(i, adj, visited, counts);
                
                // Each undirected edge is counted twice during DFS (once from each endpoint)
                int totalVertices = counts[0];
                int totalEdges = counts[1] / 2;

                // Check if the component is complete
                if (totalEdges == (totalVertices * (totalVertices - 1)) / 2) {
                    completeComponentsCount++;
                }
            }
        }

        return completeComponentsCount;
    }

    private void dfs(int u, List<List<Integer>> adj, boolean[] visited, int[] counts) {
        visited[u] = true;
        counts[0]++; // Increment vertex count
        counts[1] += adj.get(u).size(); // Add the degree of the current vertex

        for (int v : adj.get(u)) {
            if (!visited[v]) {
                dfs(v, adj, visited, counts);
            }
        }
    }
}