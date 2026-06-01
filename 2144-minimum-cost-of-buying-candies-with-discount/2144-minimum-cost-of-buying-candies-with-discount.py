class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost, reverse=True)
        c=0
        i=0
        total = 0
        while i<len(cost):
            if c<2:
                total+=cost[i]
                c+=1
            else:
                c=0
            i+=1
        return total