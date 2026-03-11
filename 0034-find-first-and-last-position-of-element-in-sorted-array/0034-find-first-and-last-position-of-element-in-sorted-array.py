class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums)-1
        l = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                l = mid if l==-1 else min(l,mid)
                right = mid-1
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        if l==-1:
            return [-1,-1]
        r = -1
        left , right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                r = max(r,mid)
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                left= mid+1

        return [l,r]

            