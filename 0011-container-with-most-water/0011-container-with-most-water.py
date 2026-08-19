class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        mw = 0
        while(l<=r):
            b = r-l
            h = min(height[l],height[r])
            mw = max(mw, b*h)
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
        return mw