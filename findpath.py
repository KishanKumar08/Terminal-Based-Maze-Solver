def path_finding(maze):


    def is_safe(mat,n,row,col):

        if row<n and col<n and (mat[row][col] == "◌" or mat[row][col] == "S" or mat[row][col] == "E"):
            return True

        return False

    def maze_path(maze,n,row,col):

        if row==n-1 and col==n-1:
            maze[row][col] = "◍"
            
            return True

        if is_safe(maze,n,row,col):

            maze[row][col] = "◍"
        
            if maze_path(maze,n,row+1,col): #move down
                return True
            if maze_path(maze,n,row,col+1): #move right
                return True
            
            maze[row][col] = "◌"
            
            return False
        
        return False

    return maze_path(maze,len(maze),0,0)