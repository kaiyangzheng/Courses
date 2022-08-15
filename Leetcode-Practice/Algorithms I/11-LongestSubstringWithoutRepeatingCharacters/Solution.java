import java.util.ArrayList;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        ArrayList<Character> substring = new ArrayList<Character>();
        int l = 0;
        int res = 0;
        
        for (int i = 0; i < s.length(); i++){
            char new_char = s.charAt(i);
            while (substring.contains(new_char)){
                substring.remove(0);
                l += 1;
            }
            substring.add(new_char);
            res = Math.max(res, i-l+1);
        }
        return res;
    }
}