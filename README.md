# PW1_Henin_CDOF5
PW1 of the dezentralisation technologies subject

Game of Life
Description

This repository contains a Python implementation of John Horton Conway's famous "Game of Life" - a cellular automaton that simulates life and death in a grid-based universe according to a set of rules. This console-based version of the game provides a simple yet fascinating demonstration of emergent behavior and pattern formation.
Features

    Grid-based Simulation: The game uses a grid where each cell can either be alive or dead.
    Random Initialization: The grid is initialized randomly, setting the stage for a unique simulation each time.
    Console Visualization: The game state is visualized in the console using a character-based representation, with '██' for live cells and spaces for dead cells, rendered within a bordered grid.
    Automatic Evolution: The grid updates at regular intervals, showing the evolution of the cell population based on the classic Game of Life rules.

Rules of the Game

The game follows these simple rules:

    Any live cell with two or three live neighbors survives.
    Any dead cell with three live neighbors becomes a live cell.
    All other live cells die in the next generation, and dead cells stay dead.

Requirements

    Python 3.x

Running the Game

    Clone this repository or download the source code.

    Navigate to the directory containing the game's Python file.

    Run the script using Python:

    bash

    python game_of_life.py

    To stop the simulation, press Ctrl + C.

Customization

You can modify the width and height variables in the script to change the size of the grid. The speed of the simulation can be adjusted by changing the time.sleep(0.5) value in the main function.
Contributing

Contributions, ideas, and feedback are welcome! Please feel free to fork the repository, create feature branches, and submit pull requests.
License

Frequently Asked Questions (FAQ):

-How do I stop the simulation?
Press Ctrl + C to stop the simulation at any time.

-Can I change the speed of the simulation?
Yes, adjust the time.sleep(0.5) value in the main function to speed up or slow down the simulation.

-Is it possible to save the current state of the game?
Feature planned for future updates.



Reporting Bugs and Requesting Features
Reporting Bugs
If you encounter any bugs, please report them via the 'Issues' tab on the GitHub repository page. Include detailed information about the bug, steps to reproduce it, and the environment in which it occurred.

Requesting Features
We welcome suggestions for new features! Feel free to open an issue to discuss potential ideas or enhancements you'd like to see in the Game of Life.



MIT License

