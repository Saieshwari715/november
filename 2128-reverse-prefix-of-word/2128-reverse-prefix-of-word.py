class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=""
        for i in range(len(word)):
            if(word[i]==ch):
                s+=word[:i+1]
                s=s[::-1]
                break
        for i in range(len(s),len(word)):
            s+=word[i]
        return s
        