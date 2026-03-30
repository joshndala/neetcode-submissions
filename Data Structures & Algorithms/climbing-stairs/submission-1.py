class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dps(step):
            if step > n:
                return 0
            if step == n:
                return 1

            return dps(step + 1) + dps(step + 2)

        return dps(0)