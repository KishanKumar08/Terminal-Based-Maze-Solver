import random

def generateMaze(size, wall_percentage):
    maze = [["◌" for col in range(size)] for row in range(size)]
    
    total_walls = int((size*size) * (wall_percentage/100))
    
    maze[0][0] = "S"
    maze[size-1][size-1] = "E"
    visited_cells = [(0,0),(size-1,size-1)]

    curr_wall_count = 0

    while (curr_wall_count!=total_walls):
        
        row = random.randint(0,size-1)
        col = random.randint(0,size-1)

        if (row,col) not in visited_cells:
            
            visited_cells.append((row,col))
            curr_wall_count+=1
            maze[row][col] = "▓"

        else:
            continue

    return maze