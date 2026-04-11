class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        while numSet:
            seq = 0
            curr = min(numSet)

            while (curr) in numSet:
                seq += 1
                numSet.remove(curr)
                curr += 1

            result = max(result, seq)

        return result