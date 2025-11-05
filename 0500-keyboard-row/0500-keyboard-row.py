class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiopQWERTYUIOP"
        row2="asdfghjklASDFGHJKL"
        row3="zxcvbnmZXCVBNM"
        a=[]
        for i in words:
            if all(j in row1 for j in i) or all(j in row2 for j in i) or all(j in row3 for j in i):
                a.append(i)
        return a  
        