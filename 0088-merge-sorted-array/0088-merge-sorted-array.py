class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k= n+m-1
        i=m-1
        j=n-1
        while i>=0 and j>=0 and k>=0:
            a = nums1[i]
            b = nums2[j]
            if a>b:
                nums1[k]=a
                i-=1
            else:
                nums1[k]=b
                j-=1
            k-=1
        
        while j>=0 and k>=0:
            nums1[k]= nums2[j]
            j-=1
            k-=1
            

                