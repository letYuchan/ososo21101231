# Runaway Game

This document explains the implementation code for the `Runaway Game`. In this game, a runner and a chaser chase each other, and the runner tries to avoid being caught for a certain period to score points.

## Key Features

- **Runner**: Moves randomly and tries to avoid the chaser.
- **Chaser**: Controlled by the user via keyboard to chase the runner.
- **Scoring System**: Points increase as long as the runner is not caught, and the final score is displayed when the game ends.
- **Timer**: The game ends after 60 seconds from the start.

## Code Explanation

### 1. Library Imports

```python
import tkinter as tk
import turtle
import random
import time
