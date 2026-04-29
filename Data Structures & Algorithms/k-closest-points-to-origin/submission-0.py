import math
import heapq
class Point:
    def __init__(self, point: List[int]):
        self.point = point
        self.x = point[0]
        self.y = point[1]
        self.dist = self.distance_form_origin()

    def distance_form_origin(self):        
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self.dist < other.dist

class KCapacityMaxHeap:
    def __init__(self, k, arr: List[List[int]]):
        points = [Point(point) for point in arr]
        topk = sorted(points, key=lambda x: x.dist)[:k]
        self.heap = heapq.heapify(topk)
        self.new_points = [[point.x, point.y] for point in topk]
    
    


        
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        KCapacityMaxHeap(k, points)
        return KCapacityMaxHeap(k, points).new_points
        