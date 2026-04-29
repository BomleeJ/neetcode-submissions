class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if frequencies.get(num) != None:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        sorted_frequencies = sorted(list(frequencies.items()), key=lambda x: x[1], reverse=True)

        return [sorted_frequencies[i][0] for i in range(k)]


            