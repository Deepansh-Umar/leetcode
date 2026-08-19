from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        l= []
        for i in freq:
            if freq[i]==i:
                l.append(i)

        if not l:
            return -1
        return max(l)