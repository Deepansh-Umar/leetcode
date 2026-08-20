class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        bs = nums[0]+nums[1]+nums[2]
        for i in range(n):
            a = nums[i]
            l = i+1
            h = n-1

            while(l<h):
                s = a+ nums[l]+nums[h]
                v1 = target-s 
                v2 = target-bs
                if (abs(v1)<=abs(v2)):
                    bs = s
                if (s>target):
                    h-=1
                else:
                    l+=1
        return bs
