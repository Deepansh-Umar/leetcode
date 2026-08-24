class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_mq(freq):
            mx = float('-inf')
            for key in freq:
                if freq[key]>= mx:
                    mx = freq[key]
            if not freq:
                return 0
            return mx
        freq = defaultdict(int)
        max_freq = 0
        i =0 
        l = 0
        ml = 0
        for j,ch in enumerate(list(s)):
            l = j-i+1
            freq[ch]+=1
            if freq[ch]>=max_freq:
                max_freq = freq[ch]
            rk = l-max_freq
            if(rk>k):
                while((j-i+1)-max_freq > k and freq[s[i]]):
                    freq[s[i]]-=1
                    i+=1
                    max_freq = get_mq(freq)
            l=j-i+1
            ml = max(l,ml)
        return ml
