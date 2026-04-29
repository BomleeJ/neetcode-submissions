import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.limit = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        nlargest = heapq.nlargest(self.limit, self.heap)
        return nlargest[-1]
