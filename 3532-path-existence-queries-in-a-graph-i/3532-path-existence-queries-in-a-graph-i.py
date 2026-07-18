class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        comp_id = [0] * n
        current_id = 0
        
        for i in range(1, n):
            
            if nums[i] - nums[i - 1] > maxDiff:
                current_id += 1
            comp_id[i] = current_id
            
       
        ans = []
        for u, v in queries:
            ans.append(comp_id[u] == comp_id[v])
            
        return ans