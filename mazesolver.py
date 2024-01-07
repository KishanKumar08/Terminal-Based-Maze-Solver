import random
from termcolor import colored

# Generate Maze Function
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

def display_maze(maze):

    total_rows = total_columns = len(maze)

    for row in range(total_rows):

        for col in range(total_columns):

            if (row == 0 and col == 0):
                print(colored(" S ","green","on_black"),end="")  
            elif (row == total_rows-1 and col == total_columns-1):
                print(colored(" E ","green","on_black"),end="")  
            elif maze[row][col] == "◌":
                print(colored(" ◌ ","blue","on_white"),end="")
            elif maze[row][col] == "▓":
                print(colored(" ▓ ","red","on_white"),end="")
            elif maze[row][col] == "◍":
                print(colored(" ◍ ","green","on_black"),end="")
            

        print()


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

def main():
    print("------------------------------")
    print(colored("  🔥 Let's Begin the Game ✨  ","blue","on_red"))
    print("------------------------------")
    maze_size = int(input("Enter the size of the maze (n*n) : "))
    wall_percent = int(input("Enter the wall percentage you want in the maze ( 1- 25 ) : "))
    
    while (wall_percent > 25 or wall_percent < 1):
        print(colored(" 🥺 Invalid Input 🥺 ","green"))
        wall_percent = int(input("Enter the wall percentage you want in the maze ( 1- 25 ) : "))

    print()
    print(colored("Generated Maze :- ","blue"))
    print()
    Maze = generateMaze(maze_size, wall_percent)
    display_maze(Maze)

    while True:

        print("1. Print The Path")
        print("2. Generate another Maze")
        print("3. Exit The Game")

        user_choice = int(input("Enter Your Choice(1/2/3) :- "))

        if user_choice == 1:
            print("Maze with path:->")
            print()
            path = path_finding(Maze)

            if (path):
                display_maze(Maze)
            else:
                print("Sorry: No Path Exist.💔 ")
                
                
            
        elif user_choice == 2:
            maze_size = int(input("Enter the size of the maze (n*n) : "))
            wall_percent = int(input("Enter the wall percentage you want in the maze ( 1- 25 ) : "))
            
            while (wall_percent > 25 or wall_percent < 1):
                print(colored(" 🥺 Invalid Input 🥺 ","green"))
                wall_percent = int(input("Enter the wall percentage you want in the maze ( 1- 25 ) : "))

            print()
            print(colored("Generated Maze :- ","blue"))
            print()
            Maze = generateMaze(maze_size, wall_percent)
            display_maze(Maze)

        elif user_choice == 3:
            print("Thank you for playing Game.❤️")
            break
            
        
        else:
            print(colored(" 🥺 Invalid Input 🥺 ","green"))
            user_choice = int(input("Enter Your Choice(1/2/3) :- "))

main()