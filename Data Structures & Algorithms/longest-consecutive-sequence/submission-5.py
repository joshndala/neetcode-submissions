class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for n in numsSet:
            if n - 1 not in numsSet:
                current = 0
                while (n) in numsSet:
                    current += 1
                    n += 1
                result = max(result, current)

        return result