class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n+1
        i = 0
        rs = 0
        for j,val in enumerate(nums):
            rs+=val
            if(rs>=target):
                res = min(j-i+1,res)
                while(rs >= target):
                    rs -= nums[i]
                    res = min(j-i+1,res)
                    i+=1
        if res==n+1:
            return 0
        return res