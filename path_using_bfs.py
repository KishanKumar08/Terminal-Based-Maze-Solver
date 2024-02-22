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


start = (0, 0)
end = (maze_size-1,maze_size-1)

# Find the shortest path using BFS
shortest_path_using_bfs = bfs(Maze, start, end)