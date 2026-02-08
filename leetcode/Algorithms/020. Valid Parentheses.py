# this code was written in 8th of January, but I had no access to internet :)))

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        open = { '(' : 1 , '{' : 2 , '[': 3 }
        close= { ')' : 1 , '}' : 2 , ']': 3 }
        stack=[]
        for char in s:
            if char in open:
                stack.append(open[char])
            elif (len(stack)==0) and (char in close):
                return False
            elif char in close and (stack[-1] == close[char]):
                stack.pop()
            elif char in close and (stack[-1] != close[char]):
                return False
        if len(stack)==0:
            return True
        else:
            return False
