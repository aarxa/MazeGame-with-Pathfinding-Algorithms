import tkinter as tk
import random
from collections import deque
import heapq

#Define the size of the maze 
WIDTH = 31 #This must be an odd number 
HEIGHT = 31 #This must be an odd number
CELL_SIZE = 20

#Directions for moving in the maze (right, left, down, up)
DIRS = [(2, 0), (-2, 0), (0, 2), (0, -2)]
MOVE_DIRS = {"Right": (1,0), "Left": (-1, 0), "Down": (0, 1), "Up": (0, -1)}

class MazeGame:
    """
    A class to represent a maze game with different pathfinding algorithms.

    This class creates a maze, intializes a graphical user Interface (GUI) using Trinter, 
    and provides various algorithms to find a path through the maze. It supports Depth-First Search (DFS), 
    Breath-First Search (BFS), Dijkstra's Algorithm, and A* Algorithm for pathfinding. The player can move
    within the maze using keyboard controls. 
    """

    def __init__(self, width, height, cell_size):
        """
        Initializing the MazeGame class. 

        Args:
            width (int): The width of the maze in cells.
            height (int): The height of the maze in cells.
            cell_size (int): The size of each cell in pixels.

        Sets up the maze, GUI components, and initializes player position. 
        """

        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.maze = self.create_maze() #Creating the maze
        self.player_pos = [0, 1] #Starting position
        self.visited = set() #Set to keep track of the visited positions
        self.root = tk.TK() #Initialize the Tkinter root window
        self.canvas = tk.Canvas(
            self.root,
            width = self.width * self.cell_size,
            height = self.height * self.cell_size,
            bg = "black",
        )

        #Creating and packing buttons for different pathfinding algorithms 
        self.canvas.pack()
        self.dfs_button = tk.Button(self.root, text="DFS", command = self.dfs_bot)
        self.dfs_button.pack(side=tk.LEFT, padx = 5, pady = 5)
        self.bfs_button = tk.Button(self.root, text="BFS", command = self.bfs_bot)
        self.bfs_button.pack(side=tk.LEFT, padx = 5, pady = 5)
        self.dijkstra_button = tk.Button(
            self.root, text = "Dijkstra", command=self.dijkstra_bot
        )
        self.dijkstra_button.pack(side=tk.LEFT, padx = 5, pady = 5)
        self.a_star_button = tk.Button(
            self.root, text = "A* Algorithm", command = self.a_star_bot
        )
        self.a_star_button.pack(side=tk.LEFT, padx = 5, pady = 5)

        #Drawing the maze and player on the canvas 
        self.draw_maze() #Draw the maze on the canvas
        self.draw_player() # Draw the player on the canvas 

        #Bind key press events to move the player
        self.root.bind("<KeyPress>", self.move_player)
        self.root.mainloop() # Start the Tkinter event loop


    def create_maze(self):
        """
        Generates a random maze using the Depth-First Search (DFS) algorithm.

        This method initializes a maze grid where all cells are initially walls. It then
        uses a stack-based approach to create a path through the maze. The path is created 
        by randomly selecting neighboring cells, marking them as part of the path, and 
        removing walls between cells. The maze is ensured to have an entrance and an exit.

        The resulting maze is a 2D list where:
        - '0' represents a path. 
        - '1' represents a wall. 

        Returns:
            list[list[int]]: A 2D list representing the generated maze. Each cell in the maze
            is either a `0` (path) or `1` (wall).

        Algorithm:
            1. Initialize the maze grid with walls (`1`).
            2. Set the starting position at `(1, 1)` as a path (`0`).
            3. Use a stack to keep track of the current path.
            4. Shuffle possible directions to ensure randomness.
            5. For each position:
                - Check the unvisited neighboring cells.
                - If there are unvisited neighbors, randomly select one, mark it as a path,
                  and remove the wall between the current cell and the neighbor.
                - If no unvisited neighbors are available, backtrack by popping the stack.
            6. Ensure there is an entrance at `(1, 0)` and an exit at `(self.height - 2, self.width - 1)`.
            7. Return the generated maze.

        Notes:
            - The maze is guaranteed to have at least one path from the entrance to the exit.
            - The `DIRS` variable should be defined elsewhere in the code, typically as a list of possible directions
              [(0, 1), (1, 0), (0, -1), (-1, 0)] representing right, down, left, and up, respectively.

        """

        maze = [
            [1 for _ in range(self.width)] for _ in range(self.height)
        ] # Start with walls everywhere
        stack = [(1,1)] # Stack to keep track of the current path
        maze[1][1] = 0 #Starting point

        while stack:
            x, y = stack[-1] #Get the current position

            #Shuffle the directions to randomize the path
            random.shuffle(DIRS)

            #Get the list of unvisited neighbors
            neighbors = [
                (x + dx, y + dy)
                for dx, dy in DIRS
                if 0 < x + dx < self.width - 1
                and 0 < y + dy < self.height - 1
                and maze[y + dy][x + dx] == 1
            ]

            if neighbors:
                nx, ny = random.choice(neighbors) #Choose a random neighbor
                stack.append((nx, ny)) #Add the neighbor to the stack
                maze[ny][nx] = 0 #Mark the neighbor as a path
                maze [ny - (ny - y) // 2][nx - (nx - x) // 2] #Remove all wall between cells
            else:
                stack.pop() #Backtrack if no unvisited neighbors
        
        #Ensuring there is a path from the start to the end
        maze[1][0] = 0 #Entrace
        maze[self.heigh - 2][self.width - 1] = 0 #Exit

        return maze