class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 hash maps
        if (len(s) == len(t)) and (set(s) == set(t)):
            smap = {}
            tmap = {}
            for letter in s:
                if smap.get(letter):
                    smap[letter] += 1
                else:
                    smap[letter] = 1
                
            for letter in t:
                if tmap.get(letter):
                    tmap[letter] += 1
                else:
                    tmap[letter] = 1
            print(tmap.values())
            print(smap.values())
            return set(tmap.values()) == set(smap.values())
        else:
            return False