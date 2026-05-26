from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            anagrams["".join(sorted(strs[i]))].append(strs[i])
        solutions = []
        for val in anagrams.values():
            solutions.append(val)
        return solutions
        