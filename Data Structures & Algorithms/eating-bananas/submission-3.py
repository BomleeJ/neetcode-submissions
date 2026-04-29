class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the range of possibilities ( i think min pile * len / h to max pile * len / h)
        lo = 1
        high = max(piles)
        
        def check_pile(k, piles, h):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
                if total_hours > h:
                    return False
            return True
        
        while lo < high:
            mid = lo + (high - lo) // 2
            if check_pile(mid, piles, h):
                high = mid
            else:
                lo = mid + 1
        return lo

                




        

                




        