class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #super inefficient, O(n)^2, brute force
        res = []

        for i, temp in enumerate(temperatures):
            res.append(0)
            for t in range(i + 1, len(temperatures)):
                if temperatures[t] > temp:
                    res[i] = t - i
                    break

        return res