class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        original = nums.copy()
        for i, j in enumerate(nums):
            product = 1
            copy = original.copy()
            del copy[i]

            for x in copy:
                product *= x

            nums[i] = product

        return nums
