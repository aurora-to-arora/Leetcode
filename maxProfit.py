class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        left = prices[0]
        best =0
        for right in prices[1:]:
            if left>right:
                left = right
            best = max(best, right-left)
        return best
