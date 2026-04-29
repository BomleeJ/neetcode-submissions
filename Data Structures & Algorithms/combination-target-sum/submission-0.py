class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # rollingSum 
        nums.sort()
        ret = []

        def BackTrak(cand, i, nums, rollingSum):
            if rollingSum == target:
                ret.append(cand.copy())
                return
            
            for idx in range(i, len(nums)):
                if rollingSum + nums[idx] > target:
                    return

                if rollingSum + nums[idx] == target:
                    ret.append(cand + [nums[idx]])
                    return 
                BackTrak(cand + [nums[idx]], idx, nums, rollingSum + nums[idx])

        BackTrak([], 0, nums, 0)
        
        return ret