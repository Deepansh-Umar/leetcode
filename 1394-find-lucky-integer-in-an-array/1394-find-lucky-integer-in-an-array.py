from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        m= -1
        for i in freq:
            if freq[i]==i:
                m = max(m,i)

        return m