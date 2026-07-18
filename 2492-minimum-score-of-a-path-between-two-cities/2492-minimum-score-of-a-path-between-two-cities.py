from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        # graph[u] will store tuples of (neighbor, distance)
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        
        # Step 2: BFS to traverse the component containing city 1
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            for neighbor, dist in graph[node]:
                # Track the minimum road weight seen in this component
                if dist < min_score:
                    min_score = dist
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score