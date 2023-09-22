import pygame

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
    # This is to add a delay to visualize the backtracking
    # make delay time 1 second for a slower visualization
    pygame.time.wait(1000)

    draw_maze()  # Update the display during each step

    # Handle events in the queue, so the window does not freeze
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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


# Pygame setup
pygame.init()
CELL_SIZE = 40  # Defines how big the cells are
SCREEN_WIDTH = CELL_SIZE * len(maze[0])
SCREEN_HEIGHT = CELL_SIZE * len(maze)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Solver')

COLORS = {
    1: (255, 255, 255),  # Wall
    0: (0, 0, 0),        # Path
    2: (0, 255, 0),      # Solution
    'start': (0, 0, 255),
    'end': (255, 0, 0)
}


def draw_maze():
    screen.fill((0, 0, 0))  # Clear the screen

    WALL_COLOR = (0, 0, 0)  # black color
    WALL_THICKNESS = 10

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            pygame.draw.rect(
                screen, COLORS[maze[i][j]], (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Draw vertical wall to the right of every cell
            pygame.draw.line(screen, WALL_COLOR, ((j+1)*CELL_SIZE, i*CELL_SIZE),
                             ((j+1)*CELL_SIZE, (i+1)*CELL_SIZE), WALL_THICKNESS)

            # Draw horizontal wall below every cell
            pygame.draw.line(screen, WALL_COLOR, (j*CELL_SIZE, (i+1)*CELL_SIZE),
                             ((j+1)*CELL_SIZE, (i+1)*CELL_SIZE), WALL_THICKNESS)

    # Draw the leftmost vertical walls and topmost horizontal walls for completeness
    pygame.draw.line(screen, WALL_COLOR, (0, 0),
                     (0, SCREEN_HEIGHT), WALL_THICKNESS)
    pygame.draw.line(screen, WALL_COLOR, (0, 0),
                     (SCREEN_WIDTH, 0), WALL_THICKNESS)

    pygame.draw.rect(screen, COLORS['start'], (start_coordinate[1] *
                     CELL_SIZE, start_coordinate[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, COLORS['end'], (destination_coordinate[1] *
                     CELL_SIZE, destination_coordinate[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()


if solve_maze(*start_coordinate):
    print("Path found!")
    draw_maze()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
else:
    print("No path available")

for row in maze:
    print(row)

pygame.quit()
