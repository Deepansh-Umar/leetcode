class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        t = s // 2
        memo = {}
        def dp(cs, i):
            if (cs, i) in memo:
                return memo[(cs, i)]
            if cs == t:
                return True
            if cs > t or i >= len(nums):
                return False
            take = dp(cs + nums[i], i + 1)
            if take:
                return True
            skip = dp(cs, i + 1)
            memo[(cs, i)] = take or skip
            return take or skip
        return dp(0, 0)