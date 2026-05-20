from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1Counts = defaultdict(int)
        str2Counts = defaultdict(int)
        for c in s:
            str1Counts[c] += 1
        for c in t:
            str2Counts[c] += 1
        return str1Counts == str2Counts
        
        