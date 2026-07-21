class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        n = len(s)
        max_gain = 0

        i = 0
        while i < n:
            if s[i] == '1':
                start1 = i
                while i < n and s[i] == '1':
                    i += 1
                end1 = i - 1

                
                if start1 > 0 and s[start1 - 1] == '0' and end1 < n - 1 and s[end1 + 1] == '0':
                    
                    left_zeros = 0
                    l = start1 - 1
                    while l >= 0 and s[l] == '0':
                        left_zeros += 1
                        l -= 1


                    right_zeros = 0
                    r = end1 + 1
                    while r < n and s[r] == '0':
                        right_zeros += 1
                        r += 1


                    max_gain = max(max_gain, left_zeros + right_zeros)
            else:
                i += 1

        return initial_ones + max_gain