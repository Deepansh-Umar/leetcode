class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> h1 = new HashMap<Character,Integer>();
        int n = s.length();
        for(int i =0;i<n;i++){
            h1.put(s.charAt(i), h1.getOrDefault(s.charAt(i),0)+1);
        }
        for(int i =0;i<n;i++){
            int a = h1.get(s.charAt(i));
            if (a==1){
                return i;
            }
        }
        return -1;
    }
}