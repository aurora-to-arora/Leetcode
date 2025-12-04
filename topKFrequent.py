class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # sort by frequency descending
        res = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        # take first k keys
        return [item[0] for item in res[:k]]
