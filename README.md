# MazeGame with Pathfinding Algorithms 

***I love developing games and I thought why not try one while learning about algorithms!***


<img width="224" alt="Screenshot 2024-08-17 at 6 32 15 PM" src="https://github.com/user-attachments/assets/df48f45f-a562-4d30-83f9-0a9cb1a96009">

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

 ## Pathfinding Algorithms Explained

### Depth-First Search (DFS)

<img src="https://github.com/user-attachments/assets/9c9f52a9-2816-43a3-b4ab-620cdfb8f7aa" alt="Depth first" width="400"/>

- Explores as far as possible along each branch before backtracking.
- Suitable for exploring large mazes but may not find the shortest path.

### Breadth-First Search (BFS)

<img src="https://github.com/user-attachments/assets/d616d7ca-7320-4533-8a37-01994aae360b" alt="BFS" width="400"/>

- Explores all possible paths level by level.
- Guarantees the shortest path in an unweighted grid.

### Dijkstra's Algorithm
<img src="https://github.com/user-attachments/assets/e579b71c-e457-48ac-ae19-e3c0c18c7df7" alt="Dijkstra" width="400"/>

- Explores paths by accumulating the smallest distance from the start node.
- Guarantees the shortest path but can be slower compared to BFS for uniform-cost grids.

### A* Algorithm

<img src="https://github.com/user-attachments/assets/d2e956fc-0529-49cf-8686-9fb51a3ca570" alt="A algorithm" width="400"/>

- Enhances Dijkstra’s by adding heuristics to guide the search.
- Typically faster and more efficient, especially in larger mazes.


## Future Improvements

- Add more algorithms (e.g., Greedy Best-First Search).
- Implement different maze generation algorithms (e.g., Prim's, Kruskal's).
- Add more customization options for the maze size and difficulty.
