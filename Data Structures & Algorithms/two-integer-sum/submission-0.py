class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Target - each value, then loop thru the value finding a match
        for idx, number in enumerate(nums):
            new_target = target - number
            for idx2, number2 in enumerate(nums):
                if idx == idx2:
                    continue
                
                if new_target == number2:
                    return [idx, idx2]

        