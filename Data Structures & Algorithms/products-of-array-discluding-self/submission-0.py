class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [-1, 0, 1, 2, 3]
        # [-1, ]
        final = []

        for idx in range(len(nums)):
            final.append([nums[idx]] * len(nums))
            final[idx][idx] = 1
            
        result = [1]*len(nums)
        for row in final:
            for idx, number in enumerate(row):
                result[idx] *= number

        return result

            
        
        