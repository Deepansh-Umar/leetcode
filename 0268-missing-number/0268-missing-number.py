class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Mathematical solution
        # n = len(nums)
        # s2 = n*(n+1)//2
        # return s2-sum(nums)

        #Bitwise Solution
        n = len(nums)
        r1 = 0
        for i in range(1,n+1):
            r1^=i
        r2 = 0
        for i in nums:
            r2^=i
        return r1^r2
