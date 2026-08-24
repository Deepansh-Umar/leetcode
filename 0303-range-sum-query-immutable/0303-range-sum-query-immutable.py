class NumArray:

    def __init__(self, nums):
        self.n = nums
        self.ps = {i:sum(nums[:i+1]) for i in range(len(nums))}

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            a = self.ps[left-1]
            b = self.ps[right]
            return self.ps[right] - self.ps[left-1]
        return self.ps[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)