class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total): #cur -> list of values added to current combination; total -> sum of combination
            if total == target:
                res.append(curr.copy()) #copy b/c we continue to use cur in other iterations
                return 

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res