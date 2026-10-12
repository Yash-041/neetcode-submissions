class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_one=0
        one_streak=0
        for n in nums:
            if n==1:
                one_streak+=1
                max_one=max(max_one,one_streak)
            else:
                one_streak=0
                
        return max_one