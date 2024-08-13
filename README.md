# MazeGame with Pathfinding Algorithms 

***I love developing games and I thought why not try one while learning about algorithms!***

## Overview
This project is a graphical maze game implemented using Python and Tkinter. It allows users to generate random mazes and play with keyboard controls.

The project also features multiple pathfinding algorithms, inclusing Depth-First Search (DFS), Breadth-First Search (BFS), Dijkstra's Algorithms, and the A* Algorithm, allowing users to visualize these algorithms in actions as they solve the maze!

## Features

- **Maze Generation:** Generates a random maze using Depth-First Search (DFS) algorithm.
- **Player Movement:** Control the player using arrow keys to navigate the maze.
- **Pathfinding Visualization:** Visualize various pathfinding algorithms:
    - **Depth-First Search (DFS):** Explores as far as possible along each brach before backtracking.
    - **Breadth-First Search (BFS):** Explores all neighbors at the present depth prior to moving on to nodes at the next depth level.
    - **Dijkstra's Algorithm:** Finds the shortest path in terms of distance (assuming uniform cost).
    - **A Algorithm:** Combinrd the best features of Breadth-First Search (BFS) and Dijkstra's to find the shortest path using heuristics.
 
## Project Structure
- ***'maze.py':*** Main script containing the 'MazeGame' class, which handles maze generation, player movement, and pathfinding algorithms.
- ***'README.md':*** Project documentation (this file).
