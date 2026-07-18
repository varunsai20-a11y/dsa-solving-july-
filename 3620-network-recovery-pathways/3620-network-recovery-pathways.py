from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :type rtype: int
        """
        n = len(online)
        
        # Step 1: Build the full graph and compute in-degrees for Topological Sort
        graph = {i: [] for i in range(n)}
        in_degree = [0] * n
        for u, v, cost in edges:
            graph[u].append((v, cost))
            in_degree[v] += 1
            
        # Step 2: Find a global Topological Order of the DAG
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, _ in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # Step 3: Collect and sort all unique edge costs for binary search
        unique_costs = sorted(list(set(cost for _, _, cost in edges)))
        
        # Helper function to check if a minimum score 'S' is achievable
        def can_achieve(S):
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                if dist[u] == float('inf') or not online[u]:
                    continue
                
                for v, cost in graph[u]:
                    if cost >= S and online[v]:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            
            return dist[n - 1] <= k

        # Step 4: Binary Search over the sorted unique costs
        low, high = 0, len(unique_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(unique_costs[mid]):
                ans = unique_costs[mid]
                low = mid + 1  # Try to look for a larger minimum edge cost
            else:
                high = mid - 1
                
        return ans