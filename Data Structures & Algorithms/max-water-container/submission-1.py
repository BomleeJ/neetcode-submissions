class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # move in a way that preserves max height while maintaining track of max area
        l, r = 0, len(heights) - 1
        area_ = lambda x, y, r, l: min(x, y) * (r - l)
        
        area = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                curr_area = area_(heights[i], heights[j], j, i)
                area = max(area, curr_area)
        
        return area

        """
        while l < r: 
            area = max(area, area_(heights[l], heights[r], r, l))

            if heights[l+1] > heights[r-1]:
                l += 1
            else:
                r -= 1
        """
        return area




        