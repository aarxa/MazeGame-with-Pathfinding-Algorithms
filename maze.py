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
