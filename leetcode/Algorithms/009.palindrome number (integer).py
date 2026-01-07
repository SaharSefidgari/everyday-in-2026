#  runtime:  4 ms    memory:  19.5 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x % 10 == 0 and x != 0)):
            return False
        else:
            rev=0
            num=x
            while rev < x:
                rev= rev*10 + num % 10
                num = num // 10
            return x==rev
