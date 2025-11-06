class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,values in dic.items():
            if(key==letter):
                p=(values/n)*100
                return int(p)
        else:
            return 0
        