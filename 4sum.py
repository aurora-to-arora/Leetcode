class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = sorted(nums)

        for idx, val in enumerate(n):
            if idx>0 and val == n[idx-1]:
                    continue
            for i in range(idx+1, len(n)):
                if i>idx+1 and n[i] == n[i-1]:
                    continue
                left, right = i+1, len(n)-1
                while left<right:
                    s = val + n[i] +n[left]+n[right]
                    if s>target:
                        right -=1
                    elif s<target:
                        left+=1
                    else:
                        res.append([val, n[i], n[left], n[right]])
                        left+=1
                        while n[left] == n[left-1] and left<right:
                            left+=1
                        
        return res
        
