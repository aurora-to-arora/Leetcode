class Solution:
    def reverse(self, x: int) -> int:

        if x==0:
            return 0
        MAX = (2**31) - 1
        MIN = -(2**31)

        if x < 0:
            sig = -1
        else:
            sig = 1

        n = abs(x)
        s = ''
        while n:
            rem = n % 10
            s += str(rem)
            n //= 10

        rev = sig * int(s)

        if rev < MIN or rev > MAX:
            return 0
        
        return rev
