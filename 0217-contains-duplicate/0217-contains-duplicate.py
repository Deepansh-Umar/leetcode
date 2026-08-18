from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #hash implementaion

        hs = defaultdict(int)
        for n in nums:
            if hs[n]>0:
                return True
            hs[n]+=1
        return False

        #set conversion

        # return len(nums)!=len(set(nums))
    
