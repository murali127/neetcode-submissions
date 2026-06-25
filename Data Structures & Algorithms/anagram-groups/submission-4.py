class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            c=[0]*26
            for j in i:
                c[ord(j)-ord('a')]+=1
            key=tuple(c)
            if key in d:
                d[key].append(i)
            else:
                d[key]=[i]
        return list(d.values())

