class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seq = []

        for c in s:
            while c in seq:
                seq.pop(0)

            seq.append(c)
            maxLength = max(maxLength, len(seq))

        return maxLength