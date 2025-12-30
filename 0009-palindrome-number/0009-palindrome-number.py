class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        rev=0
        if x<0:
            return False
        else:
            while x!=0:
                r=x%10
                rev=rev*10+r
                x=x//10
            if(rev==original):
                return True
            else:
                return False
       