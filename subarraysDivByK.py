class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count={0:1}
        prefix = 0
        res = 0

        for  n in nums:
            prefix += n
            mod = prefix%k
            if mod in count:
                res+=count[mod]
            count[mod]= count.get(mod, 0)+1
        return res
    
