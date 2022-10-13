class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        default_value = amount +1
        dp = [default_value] * (amount+1)
        dp [0] = 0
        
        for a in range(1, amount+1):
            for coin in coins:
                if a-coin >= 0:
                    dp[a] = min(1+dp[a-coin], dp[a])
                    
        min_coin = dp[amount]
        return min_coin if min_coin != default_value else -1
        
