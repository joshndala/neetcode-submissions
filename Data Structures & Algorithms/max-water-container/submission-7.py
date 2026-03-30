class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights) - 1

        while l < r:
            current = (r - l) * min(heights[l], heights[r])
            maximum = max(maximum, current)

            if heights[l] <= r:
                l += 1

            else:
                r -= 1

        return maximum