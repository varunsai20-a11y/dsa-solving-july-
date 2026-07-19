from fractions import gcd

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd = []
        current_max = nums[0]
        
        for num in nums:
            if num > current_max:
                current_max = num
            # Use the imported fractions.gcd here
            prefixGcd.append(gcd(num, current_max))
        
        prefixGcd.sort()
        
        total_gcd_sum = 0
        left = 0
        right = len(prefixGcd) - 1
        
        while left < right:
            total_gcd_sum += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum

        