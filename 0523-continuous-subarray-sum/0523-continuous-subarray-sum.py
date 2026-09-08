class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hp = {0:-1}
        n = len(nums)
        if(n<2):
            return False
        s = 0
        for i in range(n):
            s += nums[i]
            if k != 0:
                s %= k  
            if s in hp:
                if i - hp[s] >= 2:
                    return True
            else:
                hp[s] = i
        return False
        
