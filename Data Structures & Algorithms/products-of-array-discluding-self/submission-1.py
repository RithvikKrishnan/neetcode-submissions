class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(1)
        for i in range(len(nums) - 2, -1, -1):
            output[i] = nums[i + 1] * output[i + 1]
        currProduct = 1
        for i in range(len(nums)):
            output[i] = output[i] * currProduct
            currProduct = currProduct * nums[i]
        return output