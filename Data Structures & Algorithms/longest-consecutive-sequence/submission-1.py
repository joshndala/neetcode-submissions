class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        if n == 0:
            return 0
        
        longest_seq = 0

        current_seq = 1

        for i in range(1, n):
            if nums[i]-1 == nums[i-1]:
                current_seq += 1
                continue

            if nums[i] == nums[i - 1]:
                continue

            longest_seq = max(current_seq, longest_seq)
            current_seq = 1

            if i == n-1:
                longest_seq = max(current_seq, longest_seq)

        return max(current_seq, longest_seq)