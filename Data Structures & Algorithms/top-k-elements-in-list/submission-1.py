from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        pq = PriorityQueue() # min heap by defaul;t
        for num in counts:
            pq.put((counts[num], num))
            if (pq.qsize()) > k:
                _, smth = pq.get()
        answers = []
        while not pq.empty():
            answers.append(pq.get()[1])
        return answers