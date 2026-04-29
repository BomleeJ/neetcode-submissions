class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two ptrs, one is the difference and the other will be subtracted from the target
        # it will start with 0 as the difference and 1 as the subtractor. we try to find target - 1 in the remaining list. if it is not found
        # we will repeat the process be with on
        def binary_search(numbers, target, anchor):
            start = anchor + 1
            end = len(numbers) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if numbers[mid] == target:
                    return mid
                
                if target > numbers[mid]:
                    start = mid + 1
                
                if target < numbers[mid]:
                    end = mid - 1
            
            return None

        anchor = 0
        len_nums = len(numbers)

        prev = 0
        while anchor < len_nums:
            
            search_target = target - numbers[anchor]
            idx = binary_search(numbers, search_target, anchor)

            if idx and idx != anchor:
                return sorted([anchor + 1, idx + 1])

            if anchor > 0:
                prev += 1
            anchor += 1
        