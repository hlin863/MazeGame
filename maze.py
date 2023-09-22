maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start_coordinate = [8, 4]
destination_coordinate = [4, 11]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up


def is_valid(x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0


def solve_maze(x, y):
    if (x, y) == tuple(destination_coordinate):
        maze[x][y] = 2
        return True

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if is_valid(new_x, new_y):
            maze[new_x][new_y] = 2

            if solve_maze(new_x, new_y):
                return True  # Path found

            maze[new_x][new_y] = 0  # backtrack

    return False


if solve_maze(*start_coordinate):
    print("Path found!")
else:
    print("No path available")

for row in maze:
    print(row)
