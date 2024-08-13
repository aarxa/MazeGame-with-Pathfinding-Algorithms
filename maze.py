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

    Attributes:
        width (int): The width of the maze in cells.
        height (int): The height of the maze in cells.
        cell_size (int): The size of each cell in pixels.
        maze (list[list[int]]): 2D list representing the maze grid (0 for open path, 1 for wall).

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
    

    def draw_maze(self):
        """
        Draws the generated maze onto the Tkinter canvas.

        This method iterates over the 2D list representing the maze and draws each cell as a
        rectangle on the canvas. The color of the rectangle is determined by whether the cell is
        a path or a wall. The method also draws the entrance and exit of the maze with distinct colors.

        The maze is visualized as follows:
        - `0` (path) is drawn in white.
        - `1` (wall) is drawn in black.
        - The entrance is marked in green.
        - The exit is marked in red.

        Process:
            1. Iterate through each cell in the maze.
                - For each cell, determine its color based on its value (`0` or `1`).
                - Draw a rectangle representing the cell at the appropriate position on the canvas.
            2. Draw a green rectangle to represent the entrance of the maze.
            3. Draw a red rectangle to represent the exit of the maze.

        Canvas Coordinates:
            - The top-left corner of the canvas is at (0, 0).
            - Each cell's position is calculated based on its index in the maze and the cell size.
            - The entrance is drawn at the top-left corner.
            - The exit is drawn at the bottom-right corner.

        Notes:
            - The canvas is assumed to be initialized with dimensions large enough to accommodate the entire maze.
            - The entrance and exit rectangles are hardcoded to specific sizes and positions based on the cell size.

        """

        for y in range(len(self.maze)):
            for x in range(len(self.maze)):
                color = "white" if self.maze[y][x] == 0 else "black" #Path or wall
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * seld.cell_size,
                    fill=color,
                )

        #Draw the entrace
        self.canvas.create_rectangle(
            0, self.cell_size, self.cell_size, 2 * self.cell_size, fill = "green"
        )

        #Draw the exit
        self.canvas.create_rectangle(
            (self.width - 1) * self.cell_size,
            (self.height - 2) * self.cell_size,
            self.width * self.cell_size,
            (self.height - 1) * self.cell_size,
            fill = "red",
        )

    def draw_player(self):
        """
        Draws the player on the Tkinter canvas. 

        This method places a visual representation of the player at the current position on the canvas.
        The player is drawn as a blue rectangle, and it is tagged with "player" for easy identification and manipulation. 

        Process:
            1. Retrieve the current position of the player from 'self.player_pos'.
            2. Calculate the top-left and bottom-right coordinates of the rectangle representing the player based on the
                player's position and the cell size. 
            3. Draw a blue rectangle at the calculated coordinates on the canvas.
            4. Assign the tag "player" to the rectangle, which allows for easy manipulation or identification later. 
        
        Canvas Coordinates:
            - The top-left corner of the player rectangle is calculated as `(x * self.cell_size, y * self.cell_size)`.
            - The bottom-right corner of the player rectangle is calculated as `((x + 1) * self.cell_size, (y + 1) * self.cell_size)`.

        Notes:
            - The `self.player_pos` attribute should contain the current (x, y) position of the player in the maze.
            - If the player is moved or if the maze is redrawn, this method should be called to update the player's position on the canvas.
            - The "player" tag allows for potential future use cases, such as moving or updating the player's position on the canvas.

        Example:
            If `self.player_pos` is `[2, 3]` and `self.cell_size` is `20`, the player will be drawn as a blue rectangle
            from `(40, 60)` to `(60, 80)` on the canvas.

        """

        x, y = self.player_pos
        self.canvas.create_rectangle(
            x * self.cell_size,
            y * self.cell_size,
            (x + 1) * self.cell_size,
            (y + 1) * self.cell_size,
            fill = "blue",
            tags = "players",
        )

    def move_player(self, event):
        """
        Moves the player on the canvas based on keyboard input.

        This method is triggered by key press events and updates the player's position on the canvas accordingly.
        It also handles checking if the new position is valid (i.e., within maze boundaries and not a wall),
        updates the visited paths, and checks for a win condition.

        Parameters:
            event (tk.Event): The Tkinter event object containing information about the key press.

        Process:
            1. Retrieve the direction of movement based on the key pressed. `MOVE_DIRS` maps key symbols to movement offsets (dx, dy).
            2. Calculate the new position `(new_x, new_y)` by adding the direction offsets to the current player position.
            3. Check if the new position is within the maze boundaries and is a path (value of 0 in `self.maze`).
            4. If the new position is valid:
                - Mark the current position as visited by adding it to `self.visited`.
                - Update the player's position to the new coordinates.
                - Remove the previous player representation from the canvas.
                - Redraw the player at the new position.
                - Update the visualization of visited paths.
                - Check for a win condition (if the player reaches the exit) and display a "You Win!" message.

        Notes:
            - The `event.keysym` attribute provides the symbol of the key pressed, which is used to determine the direction of movement.
            - The `MOVE_DIRS` dictionary should be defined elsewhere in the class, mapping key symbols (e.g., "Up", "Down", "Left", "Right") to movement offsets.
            - The win condition is checked by comparing the player's position with the exit coordinates.

        Example:
            If the `event.keysym` is "Right" and `MOVE_DIRS` is set such that "Right" maps to `(1, 0)`, the player will move one cell to the right.
        
        """

        dx, dy = MOVE_DIRS.get(event.keysym, (0,0)) #Get the direction of movement
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        #Check if the new position is within the bounds and is the path
        if (
            0 <= new_x < self.width
            and 0 <= new_y < self.height
            and self.maze[new_y][new_x] == 0
        ):
            self.visited.add(tuple(self.player_pos))  # Mark current position as visited
            self.player_pos = [new_x, new_y]  # Update player position
            self.canvas.delete("player")  # Remove the old player position
            self.draw_player()  # Draw the new player position
            self.update_visited_paths()  # Update the visited paths

            # Check for win condition
            if new_x == self.width - 1 and new_y == self.height - 2:
                self.canvas.create_text(
                    self.width * self.cell_size / 2,
                    self.height * self.cell_size / 2,
                    text="You Win!",
                    fill="yellow",
                    font=("Helvetica", 24),
                )