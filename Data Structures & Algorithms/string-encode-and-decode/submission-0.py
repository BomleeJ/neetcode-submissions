class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            n = len(word)
            encoded += f"{n}"
            encoded += "#"
            encoded += word
        return encoded  

        
        
    def decode(self, s: str) -> List[str]:
        integer_str = ""
        word = ""
        words = []
        idx = 0
        while idx < len(s):
            try:
                int(s[idx])
                integer_str += s[idx]
            except:
                pass

            if s[idx] == "#":
                word_len = int(integer_str)
                integer_str = ""
                words.append(s[idx + 1: idx + 1 + word_len])
                idx += word_len

            idx += 1 

        return words