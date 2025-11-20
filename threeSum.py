class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet = float('-inf')
        n = sorted(nums)

        for i, val in enumerate(n):
            if i>0 and val == n[i-1]:
                continue
            left =i+1
            right = len(n)-1
            while left<right:
                c= val+n[left]+n[right]
                if c<target:
                    left+=1
                if c>target:
                    right-=1
                if abs(closet-target)>abs(c-target):
                    closet = c
                if c == target:
                    return c
        return closet
                    

        
