class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter as d
        res=[]
        vis=set()
        for i in range(len(strs)):
            p=d(strs[i])
            op=[strs[i]]
            if i in vis:
                continue
            vis.add(i)
            for j in range(i+1,len(strs)):
                if p==d(strs[j]) :
                    op.append(strs[j])
                    vis.add(j)
            res.append(op)
        return res
