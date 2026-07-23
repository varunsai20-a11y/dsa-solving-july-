class Solution:

    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1
        if n == 2:
            return 2

       
        return 1 << n.bit_length()