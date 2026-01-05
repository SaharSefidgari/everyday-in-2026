class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff=[target-x for x in nums]
        for i in range(len(nums)):
            if (diff[i] in nums) and (nums.index(diff[i]) != i):
                return [i,nums.index(diff[i])]
