class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeroes = 0
        numOnes = 0
        numTwos = 0
        for num in nums:
            numZeroes += (num == 0)
            numOnes += (num == 1)
            numTwos += (num == 2)
        index = 0
        for i in range(numZeroes):
            nums[index] = 0
            index += 1
        for i in range(numOnes):
            nums[index] = 1
            index += 1
        for i in range(numTwos):
            nums[index] = 2
            index += 1
        