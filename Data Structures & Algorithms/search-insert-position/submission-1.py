class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        mid=s+(e-s)//2
        while s<=e:
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                e=mid-1
            else:
                s=mid+1
            mid=s+(e-s)//2
            
        return mid+1