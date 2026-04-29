class Solution:
    def bt(self, final, curr, nums, idx):
        if idx == len(nums):
            curr.sort()
            final.add(tuple(curr))
            return
        
        self.bt(final, curr, nums, idx+1)
        self.bt(final, curr + [nums[idx]], nums, idx+1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = set()
        self.bt(final, [], nums, 0)
        final = [list(li) for li in final]
        return final