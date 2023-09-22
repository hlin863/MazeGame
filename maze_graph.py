import pygame

# Represent the graph in the code
graph = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': ['B', 'D', 'G'],
    'D': ['C'],
    'E': ['B', 'F', 'G'],
    'F': ['E', 'G', 'H'],
    'G': ['C', 'E', 'F'],
    'H': ['F', 'I', 'J'],
    'I': ['H'],
    'J': ['H', 'K', 'L'],
    'K': ['J'],
    'L': ['J', 'M', 'N', 'O'],
    'M': ['L'],
    'N': ['L'],
    'O': ['L']
}

# Define the start and goal nodes
start = 'A'
goal = 'O'

# Define a function to perform DFS


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited


# Find a path between start and goal using DFS
visited_nodes = dfs(graph, start, [])

# Check if the goal node was visited
if goal in visited_nodes:
    print("Path found!")
else:
    print("No path available")

# Pygame visualization setup
pygame.init()
CELL_SIZE = 40
SCREEN_WIDTH = CELL_SIZE * len(graph)
SCREEN_HEIGHT = CELL_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Graph Traversal')

COLORS = {
    'node': (0, 255, 0),
    'visited': (255, 0, 0),
    'start': (0, 0, 255),
    'goal': (255, 255, 0)
}

# Draw the graph and visualize the traversal


def draw_graph():
    screen.fill((255, 255, 255))

    for index, node in enumerate(graph):
        color = COLORS['visited'] if node in visited_nodes else COLORS['node']
        if node == start:
            color = COLORS['start']
        elif node == goal:
            color = COLORS['goal']

        pygame.draw.circle(screen, color, (index * CELL_SIZE +
                           CELL_SIZE // 2, SCREEN_HEIGHT // 2), 15)

    pygame.display.flip()


draw_graph()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
