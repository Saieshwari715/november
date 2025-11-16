class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,values in dic.items():
            if(values==1):
                return s.index(key)
                break
        else:
            return -1
    

        