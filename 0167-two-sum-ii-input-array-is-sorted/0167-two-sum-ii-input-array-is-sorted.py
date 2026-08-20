class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l,h  = 0, n-1

        while(l<h):
            s = numbers[l]+numbers[h]

            if(s==target):
                return [l+1,h+1]
            elif(s<target):
                l+=1
            else:
                h-=1

        return [-1,-1]