# mazesolver
project that will generate and solve mazes


    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = self._x1 + half_length
        y_center = self._y1 + half_length

        to_half_length = abs(to_cell._x2 - to_cell._x1) // 2
        to_x_center = to_cell._x1 + to_half_length
        to_y_center = to_cell._y1 + to_half_length

        fill_color = "blue"
        if undo:
            fill_color = "#101333"

        line = Line(Point(x_center, y_center), Point(to_x_center, to_y_center))
        self._window.draw_line(line, fill_color)