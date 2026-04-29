import heapq
class MaxHeap:
    def __init__(self, arr: List[int]):
        self.heap = [-val for val in arr]
        heapq.heapify(self.heap)

    def push(self, val):
        heapq.heappush(self.heap, -val)
        pass

    def pop(self):
        return -heapq.heappop(self.heap) if self.heap else 0

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, idx):
        return self.heap[idx]
    def empty(self):
        return self.heap == 0

class Solution:
    

    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneq = MaxHeap(stones)
        while len(stoneq) > 1: # ASSUMPTION THAT THERE ARE 2 STONES remaining
            stoneA = stoneq.pop()
            stoneB = stoneq.pop()
            newStone = stoneA - stoneB
            stoneq.push(newStone)

        return -stoneq[0]


        