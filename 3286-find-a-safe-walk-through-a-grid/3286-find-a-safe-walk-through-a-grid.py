from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # min_cost[r][c] stores the minimum health lost to reach (r, c)
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting point
        start_cost = grid[0][0]
        min_cost[0][0] = start_cost
        
        # Deque for 0-1 BFS: stores tuples of (row, col)
        queue = deque([(0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the destination, check if remaining health >= 1
            if r == m - 1 and c == n - 1:
                return health - min_cost[r][c] >= 1
            
            current_cost = min_cost[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = current_cost + grid[nr][nc]
                    
                    # If we found a strictly better path to this cell
                    if new_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = new_cost
                        
                        # 0-1 BFS optimization
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        return health - min_cost[m-1][n-1] >= 1