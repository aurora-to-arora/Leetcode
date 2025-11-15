class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        res=['' for _ in range(numRows)]
        current =0
        direction=1

        for c in s:
            res[current]+=(c)
            if current ==0:
                direction =1
            elif current == numRows-1:
                direction=-1
            current += direction

        

        return ''.join(res)
        
