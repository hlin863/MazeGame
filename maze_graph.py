import pygame
import time

# Represent the graph in the code with node positions
graph = {
    'A': {'connections': ['B'], 'position': (0, 0)},
    'B': {'connections': ['A', 'C', 'E'], 'position': (1, 0)},
    'C': {'connections': ['B', 'D', 'G'], 'position': (2, 0)},
    'D': {'connections': ['C'], 'position': (3, 0)},
    'E': {'connections': ['B', 'F', 'G'], 'position': (1, 1)},
    'F': {'connections': ['E', 'G', 'H'], 'position': (1, 2)},
    'G': {'connections': ['C', 'E', 'F'], 'position': (2, 1)},
    'H': {'connections': ['F', 'I', 'J'], 'position': (1, 3)},
    'I': {'connections': ['H'], 'position': (0, 3)},
    'J': {'connections': ['H', 'K', 'L'], 'position': (2, 3)},
    'K': {'connections': ['J'], 'position': (3, 3)},
    'L': {'connections': ['J', 'M', 'N', 'O'], 'position': (2, 4)},
    'M': {'connections': ['L'], 'position': (1, 4)},
    'N': {'connections': ['L'], 'position': (3, 4)},
    'O': {'connections': ['L'], 'position': (2, 5)}
}

start = 'A'
goal = 'O'

# Modified DFS function to be generator-based


def dfs(graph, node):
    visited = []
    stack = [node]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            yield current  # Yield the node being visited
            for neighbour in graph[current]['connections']:
                stack.append(neighbour)


# Initialize DFS
dfs_gen = dfs(graph, start)

# Pygame setup
pygame.init()
CELL_SIZE = 40
SCREEN_WIDTH = CELL_SIZE * 5  # Assuming 5x5 maze for simplicity
SCREEN_HEIGHT = CELL_SIZE * 6
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Graph Traversal')

COLORS = {
    'node': (0, 255, 0),
    'visited': (255, 0, 0),
    'start': (0, 0, 255),
    'goal': (255, 255, 0)
}


def draw_graph():
    screen.fill((255, 255, 255))

    # Draw connections first
    for node, data in graph.items():
        x1, y1 = data['position']
        for connection in data['connections']:
            x2, y2 = graph[connection]['position']
            pygame.draw.line(screen, (0, 0, 0), (x1 * CELL_SIZE + CELL_SIZE // 2, y1 * CELL_SIZE +
                             CELL_SIZE // 2), (x2 * CELL_SIZE + CELL_SIZE // 2, y2 * CELL_SIZE + CELL_SIZE // 2))

    # Draw nodes
    for node, data in graph.items():
        color = COLORS['node']
        if node in visited_nodes:
            color = COLORS['visited']
        if node == start:
            color = COLORS['start']
        elif node == goal:
            color = COLORS['goal']

        x, y = data['position']
        pygame.draw.circle(screen, color, (x * CELL_SIZE +
                           CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 15)


visited_nodes = []

running = True
while running:
    try:
        # Proceed to next step in DFS
        visited_nodes.append(next(dfs_gen))
    except StopIteration:
        # DFS complete
        pass

    draw_graph()
    pygame.display.update()
    time.sleep(1)  # Pause to show the step visually

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
