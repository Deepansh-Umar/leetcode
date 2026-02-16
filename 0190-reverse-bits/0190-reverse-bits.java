class Solution {
    public int reverseBits(int n) {
        String bs = Integer.toBinaryString(n);
        StringBuilder sb = new StringBuilder(bs);
        sb=sb.reverse();
        int k =sb.length();
        if (sb.length()<32){
            int i=0;
            
            while (i < 32-k){
                sb.append("0");
                i+=1;
            }
        }
        int l = Integer.parseInt(sb.toString(),2);
        return l;
    }
}