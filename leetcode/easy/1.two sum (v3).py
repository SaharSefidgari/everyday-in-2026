#using dictionary is way more time efficiant

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #n={index : value  for value, index in enumerate(nums)}
        mydict={}
        for i,n in enumerate(nums):
            diff= target - n
            if diff in mydict:
                return [mydict[diff] , i]
            mydict[n] = i
