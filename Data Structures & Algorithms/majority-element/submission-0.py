class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        numElements = 0
        for num in nums:
            if num == candidate:
                numElements += 1
            else:
                numElements -= 1
                if numElements < 0:
                    candidate = num
                    numElements = 1
        return candidate