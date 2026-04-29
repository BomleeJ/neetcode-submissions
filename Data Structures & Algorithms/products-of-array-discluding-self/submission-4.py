class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [4, 2, 3, 4]
        # [1, 4, 8, 24]
        # [24, 12, 4, 1]
        new = [0] * (len(nums))

        for idx, num in enumerate(nums):
            if idx == 0:
                new[idx] = 1
            else:
                new[idx] = new[idx - 1] * nums[idx - 1]
    
        post = [0] * len(nums)
        for ridx in range(len(nums) - 1, -1, -1):
            if ridx == (len(nums) - 1):
                post[ridx] = 1
            else:
                post[ridx] = post[ridx + 1] * nums[ridx + 1]
        
        result = [x * y for x, y in zip(new, post)]
      
        return result


            
        
        