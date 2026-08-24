class Solution:
    def sumGame(self, num: str) -> bool:
        num = list(num)
        c = sum([1 for _ in num if _ == "?"])
        if c % 2 != 0:
            return True
        lq = 0
        rq = 0
        n = len(num)
        sl = [0] * (n // 2)
        el = [0] * (n // 2)
        a, b = 0, 0

        for i in range(n):
            if i < (n // 2):
                if num[i] != "?":
                    sl[a] = int(num[i])
                    a += 1
                else:
                    lq += 1
            else:
                if num[i] != "?":
                    el[b] = int(num[i])
                    b += 1
                else:
                    rq += 1
        a = sum(sl)
        b = sum(el)
        diff_score = a - b
        diff_q = lq -rq
        if 2 * diff_score == -9 * diff_q:
            return False
        return True
