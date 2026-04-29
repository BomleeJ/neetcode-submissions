class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store each character in a set
        # for each character iterate thru list looking for first instance of character 
        # store maxmium window between characters
        def getidx(l, idx):
            try:
                return l[idx]
            except:
                return None

        left, right = 0, 0
        MaxW = 0
        seen = set()
        while left < len(s):
            if getidx(s, right) and s[right] not in seen:
                seen.add(s[right])
                right += 1
            else:
                MaxW = max(MaxW, len(seen))
                seen.remove(s[left])
                left += 1
        
        return MaxW



        """
        chars = set(s)

        MaxW = 0

        if len(s) == 1:
            return 1

        for char in chars:
            encounter = s.index(char)
            seen = set(char)
            for idx in range(encounter, len(s)):      
                if (s[idx] in seen) or idx == len(s) - 1:                  
                    MaxW = max(MaxW, idx - encounter)
                    encounter = idx
                seen.add(s[idx])

        return MaxW   
        """   

                    
                
            
        