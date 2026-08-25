class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ls = 0
        rs = sum(nums[1:])
        for i in range(n):
            if ls==rs:
                return i
            ls+=nums[i]
            if i==n-1:
                rs = 0
                continue
            rs-=nums[i+1]
        return -1