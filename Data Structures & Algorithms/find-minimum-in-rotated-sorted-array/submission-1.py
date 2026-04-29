class Solution:
    def findMin(self, nums: List[int]) -> int:

        def winCondition(nums, idx):
            return nums[idx - 1] > nums[idx]

        start, end = 0, len(nums) - 1
        if end == 0:
            return nums[0]
        while start <= end:
            mid = start + ((end - start) // 2) 
            if winCondition(nums, mid):
                return nums[mid]
            elif nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1



