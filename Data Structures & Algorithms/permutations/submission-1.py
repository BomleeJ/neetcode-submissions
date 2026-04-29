class Solution:
    def bt(self, final, curr, cand):
        if not cand:
            final.append(curr)
            return
        for num in cand:
            cp = cand.copy()
            cp.remove(num)
            self.bt(final, curr + [num], cp)
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        self.bt(final, [], set(nums))
        return final