from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height,):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close) # call close method when window is closed
        # Create a Canvas widget and save as data member
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        # set a data member to represent window is running and set to false
        self.__running = False

    # method we can call that will redraw all graphics in the window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # method we to set window to running and call redraw method

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("The window has closed")

    # method using the draw method of Line class to draw a line
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
    
    # method we can call to close the window
    def close(self):
        self.__running = False



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y,
            fill=fill_color,
            width=2,
        )


        
