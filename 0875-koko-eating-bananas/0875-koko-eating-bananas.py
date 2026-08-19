class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def chck(n,piles,h):
            hours = 0
            for pile in piles:
                hours += (pile + n - 1) // n

            return hours <= h

       
        ma = max(piles)
        mi = 1

        init_check = (ma*h >= sum(piles))
        if not init_check: return -1

        while (mi<=ma):
            mid = (ma+mi)//2
            if chck(mid,piles,h):
                ma = mid-1
            else:
                mi = mid+1
        return mi