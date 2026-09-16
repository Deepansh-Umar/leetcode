class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        table = [0]*(n+1)
        for i in range(n):
            v1=nums[i]
            if(i-2>=0):
                v1+=table[i-2]
            table[i]= max(v1, table[i-1])
        return table[n-1]
                

