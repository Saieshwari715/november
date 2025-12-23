class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r=[]
        p_sorted=sorted(p)
        k=len(p)
        for i  in range(len(s)-k+1):
            if(sorted(s[i:i+k])==p_sorted):
                r.append(i)
        return r
        