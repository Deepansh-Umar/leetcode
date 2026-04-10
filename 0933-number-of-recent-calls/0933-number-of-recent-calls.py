class RecentCounter:

    def __init__(self):
        self.c =0
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        v=0
        while (True):
            v = self.q[0]
            if v>=(t-3000):
                break
            else:
                self.q.pop(0)
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)