import java.util.*;
class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int p1 = 0;
        int p2 = nums.length-1;
        int res =0;
        while(p1<p2){
            int sum1 = (nums[p1]+nums[p2]);
            if(sum1 ==k) {
                res+=1; 
                p1+=1; 
                p2-=1;
                }
            else if(sum1>k) {p2-=1;}
            else{ p1+=1;}
        }
        return res;
    }
}