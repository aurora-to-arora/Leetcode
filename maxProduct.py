class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        maxp=minp=best=nums[0]

        for n in nums[1:]:
            if n<0:
                maxp, minp= minp, maxp
            maxp= max(n, maxp*n)
            minp= min(n, minp*n)
            best = max(best, maxp)
        return best
