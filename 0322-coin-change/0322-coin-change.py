class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        table = [-1]*(amount+1)
        table[0]=0
        coins = set(coins)
        for i in range(1,amount+1):
            poss = [float('inf')]
            for j in coins:
                if j<=i:
                    rem = i-j
                    if(table[rem]>=0):
                        poss.append(1+table[rem])
                    
            table[i] = min(poss)
        if(table[amount]==float('inf')):
            return -1
        return table[amount]
                    

