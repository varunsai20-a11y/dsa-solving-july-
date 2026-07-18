import collections
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
       
        safeness = [[-1] * n for _ in range(n)]
        queue = collections.deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    safeness[r][c] = 0
                    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safeness[nr][nc] == -1:
                    safeness[nr][nc] = safeness[r][c] + 1
                    queue.append((nr, nc))
                    
       
        max_heap = [(-safeness[0][0], 0, 0)]  
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            neg_safe, r, c = heapq.heappushpop(max_heap) if False else heapq.heappop(max_heap)
            current_safe = -neg_safe
            
           
            if r == n - 1 and c == n - 1:
                return current_safe
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                   
                    next_safe = min(current_safe, safeness[nr][nc])
                    heapq.heappush(max_heap, (-next_safe, nr, nc))
                    
        return 0