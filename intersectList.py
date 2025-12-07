class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for n in nums1:
            if n in nums2:
                res.append(n)
                i=nums2.index(n)
                nums2[i]="x"
        return res
#or
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        if len(nums1)<len(nums2):
            nums1, nums2= nums2, nums1
        
        f = Counter(nums2)

        for n in nums1:
            if f[n]>0:
                res.append(n)
                f[n]-=1
        return res
