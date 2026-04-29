class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [-1, 0, 1, 2, 3]
        # [-1, ]
        prefix = [0] * len(nums)
        for idx in range(len(nums)):
            if idx == 0:
                prefix[idx] = nums[idx]
            else:
                prefix[idx] = prefix[idx - 1] * nums[idx]

        suffix = [0] * len(nums)
        for idx in range(len(nums) - 1, -1, -1):
            if idx == (len(nums) - 1):
                suffix[idx] = nums[idx]
            else:
                suffix[idx] = suffix[idx + 1] * nums[idx] 

        result = [0] * len(nums)
        for idx in range(len(nums)):
            if idx == 0:
                result[idx] = suffix[idx + 1]
            elif idx == len(nums) - 1:
                result[idx] = prefix[idx - 1]
            else:
                result[idx] = prefix[idx - 1] * suffix[idx + 1]
      
        return result


            
        
        