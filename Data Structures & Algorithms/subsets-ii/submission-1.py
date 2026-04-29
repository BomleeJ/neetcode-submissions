class Solution:
    def bt(self, final, curr, nums, start):
        final.append(curr)

        for idx in range(start, len(nums)):
            if idx > start and nums[idx] == nums[idx - 1]:
                continue
            self.bt(final, curr + [nums[idx]], nums, idx+1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        self.bt(final, [], nums, 0)
    
        
        return final