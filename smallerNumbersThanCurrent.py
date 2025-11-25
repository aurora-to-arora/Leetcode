class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=sorted(nums)
        res={}
        for i, val in enumerate(n):
            if val not in res:
                res[val]=i
        ans=[]
        for i in nums:
            ans.append(res[i])
        return ans

