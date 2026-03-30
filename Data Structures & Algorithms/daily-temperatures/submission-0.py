class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Brute Force:
        # Double loop through each number, seeing how far
        # the next highest number is, or returning 0
        # Time complexity = O(n)^2

        n = len(temperatures)
        result = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break

                j += 1
                count += 1

            count = 0 if j == n else count
            result.append(count)
        
        return result