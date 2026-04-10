class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t=0
        i=0
        n=len(tickets)
        while tickets[k]>0:
            if tickets[i]>0:
                tickets[i]-=1
                if i==n-1:
                    i=0
                else:
                    i+=1
                t+=1
            else:
                if i==n-1:
                    i=0
                else:
                    i+=1
        return t