#  runtime: 11 ms    memory:  19.3 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            s=str(x)
            reversed_s = ''.join(reversed(s))
            if s==reversed_s:
                return True
            else:
                return False
