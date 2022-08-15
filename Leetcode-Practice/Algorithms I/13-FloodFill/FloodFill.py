class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        height = len(image)
        width = len(image[0])
        pixel_color = image[sr][sc]
        if pixel_color == newColor:
            return image
        
        def fill(i, j):
            if image[i][j] == pixel_color:
                image[i][j] = newColor
                if i >= 1:
                    fill(i-1, j)
                if i+1 < height:
                    fill(i+1, j)
                if j >= 1:
                    fill (i, j-1)
                if j+1 < width: 
                    fill(i, j+1)
        
        fill(sr, sc)
        return image
            