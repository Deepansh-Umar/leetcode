from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        #hashmap to store the current bucket of the number
        hs = defaultdict(int)

        #bucket
        bt = [set() for i in range(n+1)]
        for i in nums:
            curr_bucket = hs[i]
            bt[curr_bucket+1].add(i)
            if curr_bucket>0:
                bt[curr_bucket].remove(i)
            hs[i] = curr_bucket+1
        res = [0]*k
        j = 0
        i = n
        while(j<k):
            s = bt[i]
            while(s):
                res[j]= s.pop()
                j+=1
            i-=1
        return res