class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in numSet:
            if num - 1 not in numSet:
                curr = num
                seq = 0

                while curr in numSet:
                    seq += 1
                    curr += 1
                    
                result = max(result, seq)

        return result