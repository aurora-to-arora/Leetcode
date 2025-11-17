class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxa=0

        while left<right:
            w=right-left
            minh= min(height[left], height[right])
            area=w*minh
            maxa= max(area,maxa)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return maxa


        
