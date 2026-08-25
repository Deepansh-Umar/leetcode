class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #sliding window
        hs = defaultdict(int)
        hs[0]=1
        s = 0
        c = 0
        for i in range(len(nums)):
            s+=nums[i]
            if(s-goal in hs):
                c+=hs[s-goal]
            hs[s]+=1
        return c

            