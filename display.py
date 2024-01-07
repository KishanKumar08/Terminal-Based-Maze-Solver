def display_maze(maze):

    total_rows = total_columns = len(maze)

    for row in range(total_rows):

        for col in range(total_columns):

            if (row == 0 and col == 0):
                print(colored(" S  ","green","on_black"),end="  ")  
            elif (row == total_rows-1 and col == total_columns-1):
                print(colored(" E ","green","on_black"),end=" ")  
            elif maze[row][col] == "◌":
                print(colored(" ◌ ","blue","on_white"),end=" ")
            elif maze[row][col] == "▓":
                print(colored(" ▓  ","red","on_white"),end=" ")
            elif maze[row][col] == "◍":
                print(colored(" ◍ ","green","on_black"),end="  ")
            

        print()
