class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)
        if n<2:
            return nums[0]
        sl = [nums[i] for i in range(n-1)]
        sf = [nums[i] for i in range(1,n)]

        return max(self.pass1(sl), self.pass1(sf))
    def pass1(self,nums):
        n = len(nums)
        table = [0]*(n+1)
        for i in range(n):
            v1=nums[i]
            if(i-2>=0):
                v1+=table[i-2]
            table[i]= max(v1, table[i-1])
        return table[n-1]