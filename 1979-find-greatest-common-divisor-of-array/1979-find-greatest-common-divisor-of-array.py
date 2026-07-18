import fractions

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        largest = max(nums)

        return fractions.gcd(smallest,largest)
        