class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands=0
        visited=set()

        def bfs(r,c):
            q=[(r,c)]
            visited.add((r,c))
            while q:
                row,col=q.pop(0)
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))



        rows,cols=len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    bfs(r,c)
        return islands
        


