class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cs =0
        c=0
        n = len(nums)
        hs = defaultdict(int)
        hs[0]=1
        for i in range(n):
            cs += nums[i]
            if cs - k in hs:
                c += hs[cs - k]
            hs[cs] += 1
        return c