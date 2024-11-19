# Turing machine simulator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

An interactive Turing machine simulator based on automata theory, created as part of a learning project. It evaluates words based on a set of transitions defined by the user to determine their membership in a language.

## Features

- Allows configuring initial and final states.
- Supports transitions in the format `d(q,x) = (p,Y,L)`:
  - `q`: current state
  - `x`: current symbol on the tape
  - `p`: new state
  - `Y`: symbol to be written
  - `L`: head movement (`I` for left, `D` for right)
- Verifies if words belong to the defined language.

## Requirements

- **Operating System:** Windows (for executable versions).
- **Python:** Version 3.x (for script execution).

## How to run

- **GUI:** Open `turing-machine-gui.exe`. Source code in `turing-machine-gui.py`.
- **CLI:** Open `turing-machine-cli.exe`. Source code in `turing-machine-cli.py`.
- **Notebook:** Open `turing-machine-simulator.ipynb` and run the code blocks.