class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic1={}
        dic2={}
        for i in words1:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        for i in words2:
            if i in dic2:
                dic2[i]+=1
            else:
                dic2[i]=1
        c=0
        for word in dic1:
            if(dic1[word]==1 and word in dic2 and dic2[word]==1):
                c+=1
        return c
        