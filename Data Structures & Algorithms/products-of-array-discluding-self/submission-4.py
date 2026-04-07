class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i, num in enumerate(nums):
            for j, prod in enumerate(result):
                if i == j:
                    continue
                result[j] = prod * num

        return result