class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = sorted(nums)
        for idx, value in enumerate(n):
            if idx> 0 and value == n[idx-1]:
                continue
            left, right = idx+1 , len(n)-1
            while left <right:
                sum3 = value + n[left]+n[right]
                if sum3>0:
                    right -=1
                elif sum3<0:
                    left +=1
                else:
                    result.append([value, n[left], n[right]])
                    left +=1
                    while n[left] == n[left-1] and left<right:
                        left+=1
        return result  
