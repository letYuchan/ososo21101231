# Runaway Game Documentation

## Overview
The **Runaway Game** is a simple chase game implemented using Python’s **Tkinter** and **Turtle** libraries. In this game, there are two main characters: a **Chaser** (controlled by the player) and a **Runner** (controlled by AI). The Chaser's goal is to catch the Runner within 60 seconds, while the Runner attempts to avoid being caught. If the Runner avoids the Chaser for 60 seconds, the Runner wins. If the Chaser catches the Runner before the time runs out, the Chaser wins.

## Class Structure and Functionality

### 1. `RunawayGame`
The `RunawayGame` class is responsible for managing the game flow. It handles:
- Movement logic of both characters (Chaser and Runner)
- Timer and score updates
- Checking if the Chaser catches the Runner
- Game start, progress, and end conditions

#### Constructor: `__init__(self, canvas, runner, chaser, catch_radius=50)`
This initializes the game, setting up the game state and visual elements like the timer, score, and background.

- **Parameters:**
  - `canvas`: The Tkinter canvas that the game runs on.
  - `runner`: The Turtle object representing the Runner.
  - `chaser`: The Turtle object representing the Chaser.
  - `catch_radius`: The distance within which the Chaser is considered to have caught the Runner. Defaults to 50.

- **Attributes:**
  - `self.canvas`: Reference to the Tkinter canvas.
  - `self.runner` and `self.chaser`: References to the Turtle objects for Runner and Chaser.
  - `self.catch_radius2`: The squared distance used to calculate if the Chaser catches the Runner.
  - `self.start_time`: Stores the time when the game starts, used for calculating elapsed time.
  - `self.score`: Tracks how long the Runner has survived.
  - Turtle objects (`self.score_text`, `self.timer_text`, `self.caught_text`) are used to display the score, timer, and game status.

#### Method: `is_catched(self)`
- **Purpose:**  
  This function checks whether the Chaser has caught the Runner. It calculates the distance between their positions and compares it with the `catch_radius`.

- **Returns:**  
  - `True` if the distance between the Chaser and the Runner is less than the catch radius, meaning the Runner has been caught.
  - `False` otherwise.

#### Method: `update_timer(self)`
- **Purpose:**  
  This method updates the game timer, calculating the elapsed time since the game started. If the game exceeds 60 seconds and the Runner has not been caught, the game ends with the Runner winning.

- **Implementation Notes:**
  - The timer is displayed on the screen using Turtle text.
  - If the timer exceeds 60 seconds, the `end_game(won=True)` function is called to declare the Runner as the winner.

#### Method: `update_score(self)`
- **Purpose:**  
  The method increments the score if the Runner has not been caught yet. The score represents how long the Runner has survived.

#### Method: `step(self)`
- **Purpose:**  
  This is the core game loop function. It moves both the Runner and the Chaser on each iteration and checks for game state updates:
  - Updates the position of the Runner and Chaser using their respective AI.
  - Updates the score and timer.
  - Checks if the Runner has been caught using the `is_catched()` method.
  - If caught, the game ends with the Chaser winning. Otherwise, the loop continues by calling itself with a delay using `ontimer`.

#### Method: `end_game(self, won)`
- **Purpose:**  
  This method handles the game’s end state. It stops the game and displays the appropriate message based on whether the Runner or Chaser won:
  - If `won=True`, the Runner has escaped for 60 seconds.
  - If `won=False`, the Chaser has caught the Runner before 60 seconds.

#### Method: `start(self, init_dist=400, ai_timer_msec=100)`
- **Purpose:**  
  This function initializes the starting positions of both the Runner and Chaser, and sets the timer for the game loop (`step`). It sets the Runner on the left side and the Chaser on the right side of the screen.

- **Parameters:**
  - `init_dist`: The initial distance between the Runner and the Chaser.
  - `ai_timer_msec`: The interval (in milliseconds) between each step of the game loop.

### 2. `ManualMover`
This class defines the Chaser controlled by the player via keyboard inputs. It inherits from `turtle.RawTurtle` and is initialized with keyboard bindings for directional control.

#### Constructor: `__init__(self, canvas, step_move=10, step_turn=10)`
- **Parameters:**
  - `canvas`: The Tkinter canvas that the game runs on.
  - `step_move`: The distance the Chaser moves forward or backward on each key press.
  - `step_turn`: The angle by which the Chaser rotates on each turn.

- **Keyboard Bindings:**
  - `Up`: Move forward.
  - `Down`: Move backward.
  - `Left`: Turn left.
  - `Right`: Turn right.

#### Method: `run_ai(self, opp_pos, opp_heading)`
This method is a placeholder since the Chaser is manually controlled by the player, and does not require AI logic.

### 3. `SmartChaser`
This class implements an AI-controlled Chaser that automatically chases the Runner. It calculates the direction towards the Runner and moves in that direction.

#### Constructor: `__init__(self, canvas, step_move=10)`
- **Parameters:**
  - `canvas`: The Tkinter canvas that the game runs on.
  - `step_move`: The distance the Chaser moves towards the Runner on each AI step.

#### Method: `run_ai(self, runner_pos, runner_heading)`
- **Purpose:**  
  This method calculates the direction towards the Runner using the `towards()` method and moves the Chaser towards the Runner.

### 4. `SmartRunner`
The `SmartRunner` class defines the behavior of the AI-controlled Runner. The Runner moves in a random direction but strategically runs away from the Chaser if they come too close.

#### Constructor: `__init__(self, canvas, step_move=10, step_turn=10, escape_distance=150)`
- **Parameters:**
  - `canvas`: The Tkinter canvas.
  - `step_move`: Distance the Runner moves in each step.
  - `step_turn`: The angle by which the Runner can randomly turn.
  - `escape_distance`: The minimum distance the Runner tries to maintain from the Chaser. If the Chaser comes within this distance, the Runner moves away.

#### Method: `run_ai(self, chaser_pos, chaser_heading)`
- **Purpose:**  
  This method determines the Runner's movement behavior. If the Chaser is within the `escape_distance`, the Runner will turn 180 degrees and move away. Otherwise, it moves forward in a random direction and occasionally turns left or right randomly.

## Game Flow
1. **Initialization**: The game is initialized with a `RunawayGame` object, which receives the `runner` and `chaser` objects (either `SmartRunner` and `ManualMover` or `SmartChaser`).
2. **Start**: The game starts by setting the initial positions of both the Chaser and the Runner.
3. **Step Loop**: The `step()` method is called repeatedly, updating the positions of both the Chaser and Runner, updating the score and timer, and checking if the game should end.
4. **Game End**: The game ends when either:
   - The Chaser catches the Runner (`end_game(won=False)`).
   - The Runner survives for 60 seconds (`end_game(won=True)`).

## Running the Game
To run the game, use the following code in a Python environment:

```python
if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    runner = SmartRunner(screen)
    chaser = ManualMover(screen)

    runner.shape('turtle')
    runner.color('green')
    chaser.shape('turtle')
    chaser.color('red')

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()
