class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxx=0
        seen={0:-1}
        prefix = 0

        for i, val in enumerate(nums):
            if val==0:
                prefix-=1
            else:
                prefix += 1
            if prefix in seen:
                maxx= max(maxx, i-seen[prefix])
            else:
                seen[prefix]=i
        return maxx

        
