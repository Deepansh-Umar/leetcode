class Solution:
    def countBits(self, n: int) -> List[int]:
        #tabulation
        '''
        dp = [0]*(n+1)
        for i in range(n+1):
            dp[i]= dp[i>>1]+(i&1)
        return dp
        '''

        #memoization
        dp = [0]*(n+1)
        def rec(dp,i,n):
            if i==n:
                return
            dp[i]=dp[i>>1]+(i&1)
            rec(dp,i+1,n)
        rec(dp,0,n+1)
        return dp
        