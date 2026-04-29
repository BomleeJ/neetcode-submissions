class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def BackTrak(cand, avail):
            if not avail:
                return
            
            res.append(cand)
            for num in avail:
                if not cand or num > cand[-1]:
                    BackTrak(cand + [num], avail - {num})
        BackTrak([], set(nums))
        return res + [nums]
        
