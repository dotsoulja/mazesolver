from visuals import Window
from cell import Cell

def main():
    window = Window(800, 600,)
    
    c = Cell(window)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(window)
    c.has_top_wall = False
    c.draw(400, 400, 450, 450)

    c = Cell(window)
    c.has_right_wall = False
    c.draw(125, 125, 175, 175)

    c = Cell(window)
    c.has_bottom_wall = False
    c.draw(225, 225, 275, 275)

    window.wait_for_close()




if __name__ == "__main__":
    main()