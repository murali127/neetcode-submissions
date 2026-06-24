class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter as c
        a=c(s)
        b=c(t)
        return a==b
        