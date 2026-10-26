class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        current_sum=0
        minlen=float('inf')
        for r in range(len(nums)):
            current_sum+=nums[r]
            while current_sum>=target:
                minlen=min(minlen,r-l+1)
                current_sum-=nums[l]
                l+=1
            
        return 0 if minlen==float('inf') else minlen