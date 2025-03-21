from visuals import Window
from maze import Maze
import sys

def main():
    num_rows = 14
    num_columns = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_columns
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    sys.setrecursionlimit(10000)
    window = Window(screen_x, screen_y)

    maze = Maze(
        margin,
        margin,
        num_rows, 
        num_columns,
        cell_size_x,
        cell_size_y,
        window,
    )
    print("Maze created!!")
    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze can't be solved!")
    else:
        print("Maze solved!!")

    window.wait_for_close()




if __name__ == "__main__":
    main()