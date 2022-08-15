class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        def calculate_area(i, j, area, grid, width, height, visited):
            if ([i, j] in visited or i >= height or j >= width or i < 0 or j < 0 or grid[i][j] == 0):
                return area
            
            visited.append([i,j])
            area = 1 + calculate_area(i+1, j, area, grid, width, height, visited) + calculate_area(i-1, j, area, grid, width, height, visited) + calculate_area(i, j+1, area, grid, width, height, visited) + calculate_area(i, j-1, area, grid, width, height, visited)
            return area
        
        visited_coords = []
        height, width = len(grid), len(grid[0])
        max_area = 0
        for i in range(height):
            for j in range(width):
                if (grid[i][j] == 1 and [i,j] not in visited_coords):
                    area = calculate_area(i,j, 0, grid, width, height, visited_coords)
                    max_area = max(max_area, area)
        return max_area                