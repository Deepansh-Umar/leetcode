class Solution {
    public String addBinary(String a, String b) {
        int c=0;
        StringBuilder sb = new StringBuilder();
        int i =  a.length()-1;
        int j = b.length()-1;
        while(i>=0 || j>=0 || c==1){
            if (i>=0){
                c=c+ a.charAt(i)- '0'; //here a.charAt(i) = 49 if the value was 1 else 48 if it was 0 as char is converted to ascii since we try to do 0+'1'-'0'= 0+49-1
                i-=1;
            }
            if (j>=0){
                c=c+b.charAt(j)-'0'; //same as above
                j-=1;
            }
            sb.append(c%2);
            c=c/2;
        }
        return sb.reverse().toString();
    }
}