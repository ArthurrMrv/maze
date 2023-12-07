import random
import turtle
import time

from Maze import Maze
from Coordinates import Coordinates
from Graph import Graph

def main():
    global temporary_obj
    global Runing
    global m
    global screen
    global maze_walls
    global cell_width
    
    #Show usefull informations to the user, such as the commands to use 
    # turtle.hideturtle()
    # turtle.speed(0)
    # turtle.penup()
    # turtle.goto(-(cell_width*len(m.get_grid()[0])//2), (cell_width*len(m.get_grid())//2)+30)
    # turtle.write("SPACE : for solving a random start to end path\nRIGHTARROW : for changing the maze\nQ : for quit", font=("Arial", 24, "normal"))
    
    def create_maze():
        global Runing
        global m
        global screen
        global maze_walls
        global cell_width
        global temporary_obj
        if not Runing:
            Runing = True
            
            screen.tracer(0)  # Turn off screen updates to speed up rendering
            clear_tempObj()
            for w in maze_walls:
                w.clear()
            
            m = Maze(int(screen.numinput("Please enter a maze size", "", 42, minval=7, maxval=500)/2)) #Max : 250 due to screen size and screen resolution
            maze_walls, cell_width = turt_maze(screen, m.get_grid())
            
            screen.update()
            screen.tracer(1)  # Re-enable screen updates
            screen.listen()
            
            Runing = False
            
            
    def follow_path():
        global Runing
        if not Runing:
            Runing = True
            clear_tempObj()
            start = random.choice(tuple((x, y) for x in range(1, m.length, 2) for y in range(1, m.width, 2)))
            end = random.choice(tuple((x, y) for x in range(1, m.length, 2) for y in range(1, m.width, 2)))
            turt_draw_path(screen,  m.find_sol(start, end), cell_width)
            screen.listen()
            Runing = False
    
    def exit():
        global Runing
        if not Runing:
            
            screen.listen()
            screen.bye()
    
    screen.listen()
    screen.onkeypress(follow_path, 'space')
    screen.onkeypress(create_maze, 'Right')
    screen.onkeypress(exit, 'q')
    
    # Keep the window open
    turtle.done()

def turt_init(w = 600, h=600):
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Maze")
    screen.setup(width=w, height=h)
    return screen, w, h

def turt_maze(screen, maze):
    global w
    global h
    screen.tracer(0)  # Turn off screen updates to speed up rendering
    
    # Calculate cell size based on maze dimensions
    rows = len(maze)
    cols = len(maze[0])
    cell_width = h / cols
    cell_height = cell_width

    def draw_wall(x, y):
        wall = turtle.Turtle()
        wall.hideturtle()
        wall.speed(0)
        wall.penup()
        wall.color("black")
        wall.shape("square")
        wall.shapesize(cell_height / 20, cell_width / 20)
        wall.goto(x, y)
        wall.stamp()
        return wall

    def draw_maze(maze):
        walls = []
        
        for (x, y) in ((x, y) for x in range(cols) for y in range(rows)):
                if maze[y][x] == 1:
                    x_coord = x * cell_width - (w//2)
                    y_coord = (h//2) - (y + 1) * cell_height
                    walls.append(draw_wall(x_coord, y_coord))
        return walls

    # Draw the maze walls
    maze_walls = draw_maze(maze)

    # Update and display the screen
    screen.update()
    screen.tracer(1)  # Re-enable screen updates
    
    return maze_walls, cell_width

def clear_tempObj():
    global temporary_obj
    
    for obj in temporary_obj:
        obj.clear()
    temporary_obj.clear()
    
    
# Function to show a path on the maze window
def turt_draw_path(screen, path, cell_width):
    global w
    global h
    
    clear_tempObj()
    def draw_points(x, y, color):
        wall = turtle.Turtle()
        wall.hideturtle()
        wall.speed(0)
        wall.penup()
        wall.color(color)
        wall.shape("square")
        wall.shapesize((cell_width / 20)*0.80, (cell_width / 20)*0.8)
        wall.goto(x+(cell_width / 20)*0.10, y+(cell_width / 20)*0.10)
        wall.stamp()
        
        return wall
    
    # Create a turtle to draw the path
    path_turtle = turtle.Turtle()
    
    path_turtle.hideturtle()
    path_turtle.pensize(1)
    path_turtle.speed(0)
    path_turtle.penup()
    
    points= [draw_points((path[0][0] * cell_width - (w//2)), ((h//2) - (path[0][1] + 1) * cell_width), "yellow"), \
        draw_points((path[-1][0] * cell_width - (w//2)), ((h//2) - (path[-1][1] + 1) * cell_width), "blue")]
    
    path_turtle.pensize(3)
    path_turtle.speed(min(((w//cell_width)//100)*3, 10))
    path_turtle.penup()
    path_turtle.color("red")
    
    # Set the same properties as the maze turtle
    path_turtle.setx(path[0][0] * cell_width - (w//2))
    path_turtle.sety((h//2) - (path[0][1] + 1) * cell_width)
    
    # Draw the path using turtle graphics
    path_turtle.pendown()
    
    #if the path is long, we speed up the showing process  so it doesn't take ages for big mazes
    if len(path) > 20:
        
        screen.tracer(0)  # Turn off screen updates to speed up rendering
        for x, y in path[:-15]:
            path_turtle.goto(x * cell_width - (w//2), (h//2) - (y + 1) * cell_width)
            
        # Update and display the screen
        screen.update()
        screen.tracer(1)  # Re-enable screen updates
        
        for x, y in path[-15:]:
            path_turtle.goto(x * cell_width - (w//2), (h//2) - (y + 1) * cell_width)
            
    else:
        for x, y in path:
            path_turtle.goto(x * cell_width - (w//2), (h//2) - (y + 1) * cell_width)
            
            
    temporary_obj.extend(points)
    temporary_obj.append(path_turtle)

if __name__ == "__main__":
    temporary_obj = []
    Runing = False
    SECONDS : int = 7
    
    m = Maze(40)

    #print(f"Best path: {m.find_sol((1, 1), (9, 9))}")
    #print(f"Best path: {m.find_sol((1, 1), (m.length-1, m.width-1))}")
    screen, w, h = turt_init(800, 800)
    
    #Show usefull informations to the user, such as the commands to use 
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-250, 0)
    
    for i in range(SECONDS):
        turtle.write(f"The program will start in {SECONDS-i}s:\nSPACE : for solving a random start to end path\nRIGHTARROW : for changing the maze\nQ : for quit", font=("Arial", 24, "normal"))
        time.sleep(1)
        turtle.clear()
    
    maze_walls, cell_width = turt_maze(screen, m.get_grid())
    
    main()
    