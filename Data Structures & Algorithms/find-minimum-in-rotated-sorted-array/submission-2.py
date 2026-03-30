class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while nums[r] < nums[l]:
            result = nums[r]
            r -= 1

        return result