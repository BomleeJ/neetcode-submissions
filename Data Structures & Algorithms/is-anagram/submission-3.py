class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 hash maps
        if len(s) == len(t):
            return sorted(s) == sorted(t)
        return False