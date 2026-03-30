class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seq = collections.deque()
        seen = set()

        for c in s:
            while c in seen:
                seen.remove(seq.popleft())

            seq.append(c)
            seen.add(c)
            maxLength = max(maxLength, len(seq))

        return maxLength