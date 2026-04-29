class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charTable = {}
        maxFreq = 0
        max_winLen = 0
        

        l, r = 0, 0

        while r < len(s):
            if charTable.get(s[r]):
                charTable[s[r]] += 1
            else:
                charTable[s[r]] = 1
            
            maxFreq = max(maxFreq, charTable[s[r]])
            winLen = (r - l + 1)
            
            if winLen - maxFreq <= k:
                r += 1
                max_winLen = max(max_winLen, winLen) 
            else:
                charTable[s[l]] -= 1
                l += 1
                r += 1
        return max_winLen
            

