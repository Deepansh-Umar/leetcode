class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hp = {0:1}
        n = len(nums)
        c=0
        s = 0
        for i in range(n):
            s += nums[i]
            if k != 0:
                s %= k  
            if s in hp:
                c+=hp[s]
                hp[s]+=1
            else:
                hp[s] =1
            

        return c
        