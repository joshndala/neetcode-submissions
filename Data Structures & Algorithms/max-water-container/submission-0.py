class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        maxWater = 0

        for i in range(n):
            for j in range(i+1, n):
                maxWater = max(maxWater, (j-i) * min(heights[i], heights[j]))

        return maxWater