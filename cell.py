from visuals import Line, Point
import time


# Class to represent an individual cell in the maze

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
        
        
        
    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "white")
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "white")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "white")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "white")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "black")

    # method to draw a path from center of one cell to another.

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_start = self._x1 + half_length
        y_start = self._y1 + half_length

        to_half_length = abs(to_cell._x2 - to_cell._x1) // 2
        x_end = to_cell._x1 + to_half_length
        y_end = to_cell._y1 + to_half_length

        fill_color = "blue"
        if undo:
            fill_color = "black"
        # Swap start and end points if undoing the move
        if undo:
            x_start, x_end = x_end, x_start
            y_start, y_end = y_end, y_start

        # Number of segments to break the line into
        num_segments = 50  # Adjust this for smoother or chunkier drawing
        delay = 0.001 if undo else 0.00  # Delay between segments (slower for backtracking)

        # Calculate the increment for each segment
        x_increment = (x_end - x_start) / num_segments
        y_increment = (y_end - y_start) / num_segments

        # Draw the line segment by segment
        for i in range(num_segments):
            segment_start_x = x_start + i * x_increment
            segment_start_y = y_start + i * y_increment
            segment_end_x = x_start + (i + 1) * x_increment
            segment_end_y = y_start + (i + 1) * y_increment

            # Draw the current segment
            segment_line = Line(Point(segment_start_x, segment_start_y), Point(segment_end_x, segment_end_y))
            self._window.draw_line(segment_line, fill_color)
            
            self._window.redraw()  # Update the GUI to show the segment

            # Introduce a delay to slow down the drawing
            time.sleep(delay)