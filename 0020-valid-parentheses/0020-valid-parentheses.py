class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(','}':'{',']':'['}
        for char in s:
            if char in dic:
                top_ele=stack.pop() if stack else '#'
                if dic[char]!=top_ele:
                    return False
            else:
                stack.append(char)
        return not stack


        