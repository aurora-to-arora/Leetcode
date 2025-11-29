class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet= float('inf')
        n = sorted(nums)
        
        for i, val in enumerate(n):
            if i>0 and val==n[i-1]:
                continue
            left=i+1
            right = len(n)-1

            while left<right:
                current = val + n[left]+ n[right]

                if current > target:
                    right -=1
                if current < target:
                    left+=1
                if abs(closet-target)>abs(current-target):
                    closet=current
                if current == target:
                    return current
        return closet
