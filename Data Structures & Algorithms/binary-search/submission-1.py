class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        mid=s+(e-s)//2
        while s<=e:
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
            mid=s+(e-s)//2
        return -1