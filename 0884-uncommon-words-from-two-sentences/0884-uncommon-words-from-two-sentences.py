class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        r=[]
        s=s1.split()+s2.split()
        for i in s:
            if s.count(i)==1:
                r.append(i)
        return r