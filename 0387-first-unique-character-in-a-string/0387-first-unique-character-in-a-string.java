class Solution {
    public int firstUniqChar(String s) {
        int [] freq = new int[26];
        int n = s.length();
        for (int i=0;i<n;i++){
            int v = (int) s.charAt(i);
            freq[v-97]+=1;
        }
        for (int i=0;i<n;i++){
            int v = (int) s.charAt(i);
            if (freq[v-97]==1){
                return i;
            }
        }
        return -1;
    }
}