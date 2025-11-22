class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis=[1]*n

        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if nums[i]<nums[j]:
                    lis[i]=max(lis[i], 1+lis[j])
        
        return max(lis)
'''or'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        tails=[]
        for n in nums:
            p = bisect.bisect_left(tails, n)
            if p==len(tails):
                tails.append(n)
            else:
                tails[p]=n
        return len(tails)
        
