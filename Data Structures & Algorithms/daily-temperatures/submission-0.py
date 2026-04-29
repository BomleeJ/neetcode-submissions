class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmerDist = [0] * len(temperatures)
        for i in range(len(temperatures)):
            day = temperatures[i]
            for j in range((i+1), len(temperatures)):
                if temperatures[j] > day:
                    warmerDist[i] = j - i
                    break


            

        return warmerDist
        