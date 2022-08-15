class Solution {
    public String reverseWords(String s) {
        String words[] = s.split(" ");
        StringBuilder str = new StringBuilder();
        for (String word: words)
            str.append(new StringBuffer(word).reverse().toString() + " ");
        return str.toString().trim();
    }
}