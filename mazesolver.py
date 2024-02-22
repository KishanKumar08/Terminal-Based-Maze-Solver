import random
from termcolor import colored
from collections import deque

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



def bfs(maze, start, goal):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == goal:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and (maze[new_x][new_y] == "◌" or maze[new_x][new_y] == "S" or maze[new_x][new_y] == "E"):
                queue.append(((new_x, new_y), path + [current]))

    return None

def main():
    print("------------------------------")
    print(colored("  🔥 Let's Begin the Game ✨  ","blue","on_red"))
    print("------------------------------")

    while True:
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
        
        print()
        print("1. Print The Path")
        print("2. Generate another Maze")
        print("3. Exit The Game ❌")
        print()
        user_choice = int(input("Enter Your Choice(1/2/3) :- "))

        if user_choice == 1:
            print()

            start = (0, 0)
            end = (maze_size-1,maze_size-1)

            # Find the shortest path using BFS
            shortest_path_using_bfs = bfs(Maze, start, end)


            if shortest_path_using_bfs:
                for tup in shortest_path_using_bfs:
                    i,j = tup[0],tup[1]
                    Maze[i][j] = "◍"

                print("Maze with path:->")
                display_maze(Maze)
            else:
                print("Sorry: No Path Exist.💔 .")
            
            print("1. Generate another Maze")
            print("2. Exit The Game ❌")

            choice_user = int(input("Enter Your Choice(1/2):- "))

            while (choice_user != 1 and choice_user!=2):
                print(colored(" 🥺 Invalid Input 🥺 ","green"))
                choice_user = int(input("Enter Your Choice(1/2):- "))

            if choice_user == 1:
                print()
                continue
            
            else:
                print()
                print("Thank you for playing Game.❤️")
                print("----------**-------------")
                print("❤️ From Kishan Kumar.")
                break
        
        elif user_choice == 2:
            print()
            continue

            
        elif user_choice == 3:
            print()
            print("Thank you for playing Game.❤️")
            print("----------**-------------")
            print("❤️ From Kishan Kumar.")
            break
            
        
        else:
            print(colored(" 🥺 Invalid Input 🥺 ","magenta"))
            user_choice = int(input("Enter Your Choice(1/2/3) :- "))

main()