class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n=0
        a=[]
        for i in word:
            n=(n*10+int(i))%m
            if(n==0):
                a.append(1)
            else:
                a.append(0)
        return a