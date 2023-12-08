# Maze Solver

Maze Solver is a Python application that generates mazes, finds the shortest path between two points in the maze, and provides visualizations using the Turtle library.

## Features

- **Maze Generation**: Utilizes Hunt and Kill algorithm to create random maze grids efficiently.
- **Pathfinding**: Implements the A* algorithm to find the shortest path between two points in the maze.
- **Visualization**: Offers visual representations of mazes and paths using the Turtle library.
- **User Interface**: Provides a simple menu-driven interface to interact with the program.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ArthurrMrv/maze.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main file:

    ```bash
    python main.py
    ```

2. Follow the menu options:
    - Press `SPACE` to find a random path in the maze.
    - Press `RIGHT ARROW` to generate a new maze.
    - Press `C` for a classic maze with predefined start and end points.
    - Press `Q` to exit the application.

## Configuration

- Adjust the maze size and parameters in the `main.py` file.
- Modify the maze generation algorithms or pathfinding techniques in the respective modules (`Maze.py`, `Graph.py`).

## Acknowledgments

- The pathfinding algorithms is inspired by https://www.scirp.org/journal/paperinformation?paperid=70460.
- the maze generation is inspired by https://weblog.jamisbuck.org/2011/1/24/maze-generation-hunt-and-kill-algorithm.
- The Turtle library provides the graphical interface for the project.
