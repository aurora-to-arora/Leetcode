class NumArray:

    def __init__(self, nums: List[int]):
        self.res=[0]
        for n in nums:
            self.res.append(self.res[-1]+n)

    def sumRange(self, left: int, right: int) -> int:
        return self.res[right+1]-self.res[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

#or

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
