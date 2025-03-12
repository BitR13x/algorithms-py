with open("maze.txt", "r") as f:
    maze = [line.strip().split(" ") for line in f.readlines()]


start = None
finish = None
def print_maze(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            print(maze[x][y], end=" ")
        print()


for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == "S":
            start = (x, y)
        
        if maze[x][y] == "C":
            finish = (x, y)

if start == None or finish == None:
    print("Cannot find exit or start")
    exit()

def get_choices(current_position: tuple[int, int]):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                # D, N, L, P
    choices = []
    for dx, dy in directions:
        choices.append((current_position[0] + dx, current_position[1] + dy))

    return choices


def is_valid(x: int, y: int, maze: list[list[str]]):
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
        return False
    
    if maze[x][y] == "#":
        return False
    
    return True


def reconstruct_path(came_from: dict, node: tuple[int, int]):
    total_path = [node]
    while node in came_from.keys():
        node = came_from[node]
        total_path.append(node)
    return total_path[::-1]

from os import system
from time import sleep
def DFS(start, finish, maze):
    stack = [start]
    visited = set()
    came_from = {}

    while stack:
        node = stack.pop()

        # printing if
        if maze[node[0]][node[1]] != "C":
            maze[node[0]][node[1]] = "X"
            print_maze(maze)
            sleep(.2)
            system('clear')


        if node == finish:
           return reconstruct_path(came_from, node)


        for x, y in get_choices(node):
            if is_valid(x, y, maze) and not (x, y) in visited:
                visited.add(node)
                stack.append((x, y))
                # transcribe num to dir
                came_from[(x, y)] = node

    return False


def transcribe_path(path: list[tuple[int, int]]):
    result = ""
    for i in range(len(path)-1):
        for dn, dl in zip([(-1, 0), (1, 0), (0, -1), (0, 1)], ["U", "D", "L", "R"]):
            if (path[i][0] + dn[0], path[i][1] + dn[1]) == path[i+1]:
                # I went here
                maze[path[i][0] + dn[0]][path[i][1] + dn[1]] = "O"
                print_maze(maze)
                sleep(.2)
                system('clear')
                ###

                result += dl

    return result

path = DFS(start, finish, maze)
if path:
    print("Shortest Path:", path)
    print("Transcribed Path:", transcribe_path(path))
else:
    print("No path found!")


print_maze(maze)