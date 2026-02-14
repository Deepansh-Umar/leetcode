class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        md = float('inf')
        t=n-k+1
        for i in range(t):
            min1 = nums[i]
            max1 = nums[k+i-1]
            diff = max1-min1
            md = min(diff,md)
        return md
