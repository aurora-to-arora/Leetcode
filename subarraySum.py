class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1} #0 came 1 time
        current =0
        count = 0

        for n in nums:
            current += n
            if current -k  in freq:
                count += freq[current-k]
            freq[current]= freq.get(current,0)+1
        return count
