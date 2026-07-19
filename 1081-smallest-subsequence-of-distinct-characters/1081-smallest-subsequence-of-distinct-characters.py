class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for idx, char in enumerate(s):
           
            if char in seen:
                continue
                
          
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
           
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)