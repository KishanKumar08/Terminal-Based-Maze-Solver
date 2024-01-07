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
        print("2. Generate another Puzzle")
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