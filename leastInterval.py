class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxf = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxf)

        blocks = (maxf - 1) * (n + 1) + maxCount

        return max(blocks, len(tasks))
