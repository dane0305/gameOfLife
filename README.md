# gameOfLife
Python code implementation of Conway's game of life, design for JdeRobot python challenge 2021.
It only uses python standard libraries so it's not necessary to install additional libraries.
The game is printed into the console, '#' means live cells while '.' means dead cells.
Code created by Daniel Rojas.

The module `gameOfLife` has the functions `runGame`, `printGrid`, `continueGame`, `nextGeneration`, `initializeGrid` and `startGame`. The only funtion that has to be called is `runGame`.
The test file tests the functions `continueGame`, `nextGeneration` and `initializeGrid`.

The file `configurations` contains all the patterns that can be used in the generation of the initial grid, also you can change the default rows and columns. This file is in format json.
