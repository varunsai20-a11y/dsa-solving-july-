import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        
        
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1
            
        gcd_count = [0] * (max_val + 1)
        
        for g in range(max_val, 0, -1):
            
            multiples = 0
            for k in range(g, max_val + 1, g):
                multiples += cnt[k]
                
            
            total_pairs_divisible = (multiples * (multiples - 1)) // 2
            
            
            for k in range(2 * g, max_val + 1, g):
                total_pairs_divisible -= gcd_count[k]
                
            gcd_count[g] = total_pairs_divisible
            
        
        prefix_sums = []
        gcd_elements = []
        current_total = 0
        
        for g in range(1, max_val + 1):
            if gcd_count[g] > 0:
                current_total += gcd_count[g]
                prefix_sums.append(current_total)
                gcd_elements.append(g)
                
        
        answer = []
        for q in queries:
            
            idx = bisect.bisect_right(prefix_sums, q)
            answer.append(gcd_elements[idx])
            
        return answer

        