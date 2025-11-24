class Solution:
    def containsDuplicate(self, n: List[int]) -> bool:
        return not len(set(n))==len(n)

# time complexity - O(n)
#space complexity- O(n)
        
