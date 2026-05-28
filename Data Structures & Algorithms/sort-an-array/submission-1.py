from collections import defaultdict
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        sortedNums = []
        for i in range(-50000, 50001):
            for k in range(counts[i]):
                sortedNums.append(i)
        return sortedNums

        