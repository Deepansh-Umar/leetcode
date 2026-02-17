class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        k= len(nums)-1
        i=0
        j = len(nums)-1
        while i<=j:
            a= nums[i]**2
            b= nums[j]**2
            if a>b:
                arr[k]=a
                i+=1
            else:
                arr[k]=b
                j-=1
            k-=1
        return arr 