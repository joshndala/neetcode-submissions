class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {} #num -> index

        for i, n in enumerate(nums):
            numsMap[n] = i

        for i, n in enumerate(nums):
            result = target - n
            if result in numsMap and numsMap[result] != i:
                return [i, numsMap[result]]