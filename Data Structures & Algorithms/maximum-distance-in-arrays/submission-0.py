class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # find the minimum
        # find the maximum
        # if minimum and maximum are in same spot repeat the process twice
        # once keeping minimum in the same spot and searching for a different maximum
        # the other keeping maximum in the same spot and searching for different minimum
        
        currMin = globalMin = arrays[0][0]
        currMax = globalMax = arrays[0][-1]

        diff = 0

        for idx in range(1, len(arrays)):
            arr = arrays[idx]

            currMin = arr[0]
            currMax = arr[-1]

            diff = max(diff, abs(globalMax - currMin), abs(currMax - globalMin))

            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        return diff


