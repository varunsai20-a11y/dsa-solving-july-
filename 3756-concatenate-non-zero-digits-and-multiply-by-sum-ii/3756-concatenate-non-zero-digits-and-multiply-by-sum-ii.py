class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        MOD = 10**9 + 7
        
       
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + int(s[i])
            
       
        suffix_val = [0] * (n + 1)
        cnt_nonzero = [0] * (n + 1)
        
        current_power = 1
        for i in range(n - 1, -1, -1):
            digit = int(s[i])
            if digit != 0:
                cnt_nonzero[i] = cnt_nonzero[i + 1] + 1
                suffix_val[i] = (suffix_val[i + 1] + digit * current_power) % MOD
                current_power = (current_power * 10) % MOD
            else:
                cnt_nonzero[i] = cnt_nonzero[i + 1]
                suffix_val[i] = suffix_val[i + 1]
        
       
        inv_pow10 = [1] * (n + 1)
        inv_10 = pow(10, MOD - 2, MOD)  
        for i in range(1, n + 1):
            inv_pow10[i] = (inv_pow10[i - 1] * inv_10) % MOD
            
        ans = []
        
       
        for l, r in queries:
            digit_sum = pref_sum[r + 1] - pref_sum[l]
            
            if digit_sum == 0:
                ans.append(0)
                continue
            
           
            raw_window_val = (suffix_val[l] - suffix_val[r + 1]) % MOD
            
            
            trailing_nonzero_count = cnt_nonzero[r + 1]
            
            x = (raw_window_val * inv_pow10[trailing_nonzero_count]) % MOD
            
            ans.append((x * digit_sum) % MOD)
            
        return ans