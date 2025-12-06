class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len= len(words[0])
        total = word_len+len(words)
        need= Counter(words)
        res=[]

        for start in range(word_len):
            left=start
            window= Counter()
            count = 0

            for right in range(start, len(s)-word_len+1, word_len):
                word = s[right:right+word_len]

                if word in need:
                    window[word]+=1
                    count+=1


                    while window[word]>need[word]:
                        left_word=s[left:left+word_len]
                        window[left_word]-=1
                        left+=word_len
                        count-=1
                    
                    if count == len(words):
                        res.append(left)
                else:
                    window.clear()
                    count=0
                    left=right+word_len

        return res
