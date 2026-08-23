class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        i = 0
        mc = 0
        for j, fruit in enumerate(fruits):
            count[fruit] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            mc = max(mc, j - i + 1)
        return mc