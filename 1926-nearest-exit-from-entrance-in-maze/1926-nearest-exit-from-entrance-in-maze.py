from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n =len(maze)
        m = len(maze[0])
        visited = set()
        queue = deque([tuple(entrance+[0])])
        soln = []
        while(queue):
            cell = queue.popleft()
            i,j  = cell[0],cell[1]
            if((i,j) in visited):
                continue
            visited.add((i,j))
            combo = [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]
            steps = cell[2]
            if((i-1 == -1 or i+1 ==n or j-1 == -1 or j+1 ==m) and steps!=0):
                return steps
            for i,j in combo:
                if(i>=0 and i<n and j>=0 and j<m):
                    if (maze[i][j] == "." and ((i,j) not in visited)):
                        queue.append((i,j,steps+1))
        
        return -1
