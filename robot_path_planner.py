"""A small, dependency-free A* path planner for a 2D robot grid.
Run: python robot_path_planner.py
"""
from heapq import heappop, heappush

GRID = [
    "S...#......",
    ".##.#.####.",
    "...#....#..",
    ".#####..#..",
    "......#...G",
]
START = (0, 0)
GOAL = (4, 10)

def neighbours(node):
    r, c = node
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(GRID) and 0 <= nc < len(GRID[0]) and GRID[nr][nc] != '#':
            yield nr, nc

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def plan(start, goal):
    frontier, came_from, cost = [(0, start)], {start: None}, {start: 0}
    while frontier:
        _, current = heappop(frontier)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for nxt in neighbours(current):
            new_cost = cost[current] + 1
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                heappush(frontier, (new_cost + heuristic(nxt, goal), nxt))
                came_from[nxt] = current
    return []

path = plan(START, GOAL)
rendered = [list(row) for row in GRID]
for r, c in path[1:-1]:
    rendered[r][c] = '*'
print("A* ROBOT PATH PLANNER")
print("Path length:", len(path) - 1, "moves")
print("\n".join("".join(row) for row in rendered))
