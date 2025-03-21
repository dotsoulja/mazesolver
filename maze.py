from cell import Cell
import random
import time


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_size_x,
            cell_size_y,
            window=None,
            seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    
    def _create_cells(self):
        for i in range(self._num_columns):
            column_cells = []
            for j in range(self._num_rows):
                column_cells.append(Cell(self._window))
            self._cells.append(column_cells)
        for i in range(self._num_columns):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        # calculate the x/y coordinates of cell bassed on i, j, cell size
        # and x/y of the maze itself
        if self._window is None:
            return
        
        x1 = self._x1 + j * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        # Method that allows us to visualize maze being built, call windows redraw method
        # then use time.sleep() so eyes can kep up with each render

        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # Method to break the entrance and exit of the maze
        # by removing the walls of the first and last cells
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_columns -1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_columns - 1, self._num_rows - 1)


    # recursive method to travel through the maze, breaking walls as it goes.
    # using a depth-first search algorithm

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            # determine which cell(s) we can move to next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_columns - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go, break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            # Randomly choose a direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock down the wall between the current cell and the next cell
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
        

 