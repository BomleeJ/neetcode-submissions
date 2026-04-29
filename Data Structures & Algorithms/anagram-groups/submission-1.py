class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash map with indicies as the values and the sorted anagrams as the key
        # build a list of that hashmap
        anagrams = {}
        for idx, word in enumerate(strs):
            frequencies = [0 for i in range(26)]
            for char in word:
                frequency_idx = ord(char) - ord('a')
                frequencies[frequency_idx] += 1
            frequencies = tuple(frequencies)
            if anagrams.get(frequencies) == None:
                anagrams[frequencies] = [strs[idx]]
            else:
                anagrams[frequencies].append(strs[idx])
            
        return list(anagrams.values())

        