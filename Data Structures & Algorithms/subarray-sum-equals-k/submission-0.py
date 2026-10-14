class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        currentSum=0
        res=0
        diff=0
        for n in nums:
            currentSum+=n
            diff=currentSum-k
            res+=prefix.get(diff,0)
            prefix[currentSum]=1+prefix.get(currentSum,0)

        return res
