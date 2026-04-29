class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Target - each value, then loop thru the value finding a match
        targets = {} # new_target: idx #we have a number, search for the difference
        for idx, number in enumerate(nums):
            new_target = target - number
            if targets.get(new_target) != None:
                print([targets[new_target], idx])
                return [targets[new_target], idx]
            targets[number] = idx

