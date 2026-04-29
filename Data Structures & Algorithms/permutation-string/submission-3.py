class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Sliding Window of len(s1)
        # for every character in the s2 window, there exists an analogue in s1
        l, r = 0, len(s1) - 1

        match_count = 0
        s1freq = {}
        for char in s1:
            s1freq[char] = s1freq.get(char, 0) + 1

        s2freq = {}
        for char in s2[l:(r+1)]:
            s2freq[char] = s2freq.get(char, 0) + 1
            if s1freq.get(char) and s1freq[char] == s2freq[char]:
                match_count += s1freq[char]

        while True:
            if match_count == len(s1):
                return True
            else:
                oldChar = s2[l]
                if s1freq.get(oldChar) == s2freq.get(oldChar):
                    match_count -= 1 # of .get(l, 0)
                
                
                s2freq[oldChar] -= 1 # we can delete to optimize space if it is 0
                
                if s2freq[oldChar] == 0:
                    del s2freq[oldChar]

                
                l += 1
                r += 1

                if r >= len(s2):
                    break


                newChar = s2[r]
                s2freq[newChar] = s2freq.get(newChar, 0) + 1
                
                if s1freq.get(newChar) and s1freq[newChar] == s2freq[newChar]:
                    match_count += s1freq[newChar]
                

        return False