from collections import deque
import pygame


def is_valid(x, y):
    # Check if the current position is valid
    # (within the maze bounds and not a wall and is a letter)
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and (maze[x][y] == 0 or maze[x][y] in letter_number_dictionary.values())


maze = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [2, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 4, 0, 0, 0, 5],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 6, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 14, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 8, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 9, 0, 0, 0, 11, 0, 0, 0, 0, 0, 13, 16],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 10, 1, 1, 1, 12, 1, 1, 1, 1, 1, 15, 1]
]

letter_number_dictionary = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 5,
    'E': 6,
    'F': 7,
    'G': 8,
    'H': 9,
    'I': 10,
    'J': 11,
    'K': 12,
    'L': 13,
    'M': 14,
    'N': 15,
    'O': 16
}

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

start_coordinate = [0, 1]
destination_coordinate = [12, 15]

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 700
CELL_SIZE = WIDTH // len(maze[0])
ROWS, COLS = len(maze), len(maze[0])
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze BFS Visualization")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

color_map = {
    0: WHITE,
    1: BLACK,
    2: RED,
    3: GREEN,
    4: GREEN,
    5: GREEN,
    6: GREEN,
    7: GREEN,
    8: GREEN,
    9: GREEN,
    10: GREEN,
    11: GREEN,
    12: GREEN,
    13: GREEN,
    14: GREEN,
    15: GREEN,
    16: GREEN
}


def draw_window():
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(
                WIN, color_map[maze[i][j]], (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.line(WIN, YELLOW, (j*CELL_SIZE, i *
                             CELL_SIZE), (j*CELL_SIZE, (i+1)*CELL_SIZE))
            pygame.draw.line(WIN, YELLOW, (j*CELL_SIZE, i *
                             CELL_SIZE), ((j+1)*CELL_SIZE, i*CELL_SIZE))

    pygame.display.update()


def bfs_visualization(start, end):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    draw_window()
    running = True
    while queue and running:
        (x, y), path = queue.popleft()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (x, y) == end:
            for px, py in path:
                maze[px][py] = 2
                draw_window()
                pygame.time.delay(50)
            break

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                maze[new_x][new_y] = 2  # Mark visited node
                new_path = path + [(x, y)]
                queue.append(((new_x, new_y), new_path))
                draw_window()
                pygame.time.delay(50)  # Delay for visualization effect


bfs_visualization(start_coordinate, destination_coordinate)
pygame.quit()
