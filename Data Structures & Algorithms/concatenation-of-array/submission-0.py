class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2 * len(nums)):
            index = i
            if (index >= len(nums)):
                index -= len(nums)
            ans.append(nums[index])
        return ans
        