class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p,n=0,1
        res=[0]*len(nums)
        for num in nums:
            if num<0:
                res[n]=num
                n+=2
            else:
                res[p]=num
                p+=2
        return res
        