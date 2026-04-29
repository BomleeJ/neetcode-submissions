class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash map with indicies as the values and the sorted anagrams as the key
        # build a list of that hashmap
        anagrams = {}
        for idx, word in enumerate(strs):
            sorted_word = ''.join(sorted(word))
            if anagrams.get(sorted_word) == None:
                anagrams[sorted_word] = [strs[idx]]
            else:
                anagrams[sorted_word].append(strs[idx])
            
        return list(anagrams.values())
            