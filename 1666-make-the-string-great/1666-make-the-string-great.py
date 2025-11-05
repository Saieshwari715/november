class Solution:
    def makeGood(self, s: str) -> str:
        a=[]
        for i in s:
            if a and a[-1]!=i and a[-1].lower()==i.lower():
                a.pop()
            else:
                a.append(i)
        return "".join(a)

        