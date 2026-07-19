class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []
        for i in range(len(nums)):
            right.append(1)
            left.append(1)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        for i in range(len(nums) - 1):
            left[i + 1] = nums[i] * left[i]
        output = []
        for i in range(len(nums)):
            output.append(right[i] * left[i])
        return output
        