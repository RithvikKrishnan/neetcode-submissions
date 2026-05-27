class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newIndex = 0
        for num in nums:
            if num != val:
                nums[newIndex] = num
                newIndex += 1
        return newIndex
        