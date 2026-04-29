class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        count = 0
        while True:
            if len(nums_set) == 0:
                return count
            nums_set = set(filter(lambda x: x-1 in nums_set, nums_set))
            count += 1