class Solution {
    public void fill(int sr, int sc, int height, int width, int color, int newColor, int[][] image){
        if (image[sr][sc] == color){
            image[sr][sc] = newColor;
            if (sr >= 1){
                fill(sr-1, sc, height, width, color, newColor, image);
            }
            if (sr + 1 < height){
                fill(sr+1, sc, height, width, color, newColor, image);
            }
            if (sc >= 1){
                fill(sr, sc-1, height, width, color, newColor, image);
            }
            if (sc + 1 < width){
                fill(sr, sc+1, height, width, color, newColor, image);
            }
        }
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int height = image.length;
        int width = image[0].length;
        int pixelColor = image[sr][sc];
        if (pixelColor == newColor){
            return image;
        }
        
        fill(sr, sc, height, width, pixelColor, newColor, image);
        return image;
    }
}