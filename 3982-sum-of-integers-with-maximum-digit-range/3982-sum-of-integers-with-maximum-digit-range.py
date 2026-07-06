class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:


        def getmaxmin(n):
            m = float("-inf")
            mi = float("inf")
            a=0
            while n>0:
                a = n%10
                m = max(a,m)
                mi = min(a,mi)
                n=n//10
            return m-mi



        m1 = float("-inf")
        h = [0]*len(nums)
        i=0
        for num in nums:
            diff = getmaxmin(num)
            m1 = max(m1,diff)
            h[i]=diff
            i+=1
        s= 0
        for i in range(len(nums)):
            if h[i]==m1:
                s+=nums[i]
        return s