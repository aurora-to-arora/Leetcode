class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            max_i = arr.index(size)

            if max_i == size - 1:
                continue

            if max_i != 0:
                res.append(max_i + 1)
                arr[:max_i + 1] = reversed(arr[:max_i + 1])

            res.append(size)
            arr[:size] = reversed(arr[:size])

        return res
