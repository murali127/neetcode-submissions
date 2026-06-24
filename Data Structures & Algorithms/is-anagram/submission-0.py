class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st="".join(sorted(t))
        ts="".join(sorted(s))
        if st==ts:
            return True
        else:
            return False