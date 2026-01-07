class Solution:
    def romanToInt(self, s: str) -> int:
        symbol= {
            'I':             1,
            'V':             5,
            'X':            10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000
        }
        exeption = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        result = 0
        i=0
        while i in range(0,len(s)):
            if i < len(s)-1:
                if symbol[s[i]] >= symbol[s[i+1]]:
                    result += symbol[s[i]]
                    i += 1
                elif s[i:i+2] in exeption.keys():
                    result += exeption[s[i:i+2]]
                    i += 2
            else:
                result += symbol[s[i]]
                i += 1
        return result
