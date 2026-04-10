class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int t =0;
        int i=0;
        int n = tickets.length;
        while(tickets[k]>0){
            if (tickets[i]>0){
                tickets[i]-=1;
                if (i==n-1){
                    i=0;
                }
                else{
                    i+=1;
                }
                t+=1;
            }
            else{
                if (i==n-1){
                    i=0;
                }
                else{
                    i+=1;
                }
            }
        }
        return t;
    }
}