class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        H=heights[0]
        l,r=0,len(heights)-1
        while l<r:
            H=min(heights[l],heights[r])
            B=r-l
            max_area=max(max_area,(H*B))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area