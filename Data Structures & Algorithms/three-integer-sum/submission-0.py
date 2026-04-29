class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, target in enumerate(nums):
            if target > 0:
                break

            if idx > 0 and target == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            while l < r:
                sigma3 = target + nums[l] + nums[r]
                if sigma3 > 0:
                    r -= 1
                elif sigma3 < 0:
                    l += 1
                else:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res





