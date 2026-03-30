class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]

            res = amount + 1
            for coin in coins:
                if a - coin >= 0:
                    res = min(res, 1 + dfs(a - coin))

            memo[a] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= amount + 1 else minCoins