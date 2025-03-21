from visuals import Window
from maze import Maze

def main():
    num_rows = 12
    num_columns = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_columns
    cell_size_y = (screen_y - 2 * margin) / num_rows
    window = Window(screen_x -175, screen_y + 150)

    maze = Maze(
        margin,
        margin,
        num_rows, 
        num_columns,
        cell_size_x,
        cell_size_y,
        window,
        10,
    )

    window.wait_for_close()




if __name__ == "__main__":
    main()