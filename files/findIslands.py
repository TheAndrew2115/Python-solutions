'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.
'''

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    num = 0
    
    def project(grid, start, islands): # start: [x,y] make sure you start on 1
        islands.append(start)
        for d in directions:
            x = start[0] + d[0]
            y = start[1] + d[1]
            point = [x,y]
            if point[0] >= 0 and point[1] >= 0 and point[0] < m and point[1] < n:
                if grid[point[0]][point[1]] == 1and point not in islands:
                    project(grid, point, islands)
    
    islands = [] 
    #  This would be much faster if islands was a set, then the lookup time
    #  for something in islands would be O(1) instead of O(n)
    
    for i in range(0,m):
        for j in range(0,n):
            if grid[i][j] == 1 and [i,j] not in islands:
                project(grid,[i,j],islands)
                num+=1
    print(islands)
    return num

# grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
# grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
# grid = [[1,0],[0,1]]
# grid = [[1,1,0,1],[1,0,1,0],[0,0,1,1],[1,1,0,0]]
grid = [[]]
print(numIslands(grid))
