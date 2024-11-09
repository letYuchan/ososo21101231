import tkinter as tk
import turtle
import random
import time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius ** 2
        self.start_time = time.time()  # Record start time
        self.score = 0  # Initial score

        # Turtle object for score and timer
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        # Background setup
        self.canvas.bgcolor("lightblue")  # Change background color

        # Save score and timer text
        self.score_text = self.drawer.clone()  # Clone turtle for score text
        self.timer_text = self.drawer.clone()  # Clone turtle for timer text
        self.caught_text = self.drawer.clone()  # Clone turtle for state text

        self.score_text.setpos(-300, 300)  # Set score position
        self.timer_text.setpos(-300, 250)  # Set timer position
        self.caught_text.setpos(-300, 220)  # Set state text position

    def is_catched(self):
        """ Check if the runner is caught by the chaser """
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx ** 2 + dy ** 2 < self.catch_radius2

    def update_timer(self):
        """ Update elapsed time and display it """
        elapsed_time = time.time() - self.start_time
        self.timer_text.clear()  # Clear previous timer text
        self.timer_text.write(f'Time: {elapsed_time:.2f}', move=False)

        # End game after 60 seconds
        if elapsed_time > 60:  # After 60 seconds
            self.end_game(won=True)  # Update to indicate the runner won

    def update_score(self):
        """ Update score; increase if the runner is not caught """
        if not self.is_catched():
            self.score += 1
        return self.score

    def step(self):
        """ Move runner and chaser in each game step """
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        is_catched = self.is_catched()

        # Display score and state
        self.score_text.clear()  # Clear previous score text
        self.caught_text.clear()  # Clear previous state text

        self.score_text.write(f'Score: {self.update_score()}', font=("Arial", 16, "normal"))
        self.caught_text.write(f'Is catched? {is_catched}', font=("Arial", 16, "normal"))

        # Update timer
        self.update_timer()

        # End game if caught
        if is_catched:
            self.end_game(won=False)
        else:
            # Set timer for next step
            self.canvas.ontimer(self.step, self.ai_timer_msec)

    def end_game(self, won):
        """ Function called on game end """
        self.drawer.setpos(-200, 0)
        if won:
            self.drawer.write("You loose! The runner escaped!", font=("Arial", 24, "normal"))  # Runner escapes message
        else:
            self.drawer.write("You WIN! you caught the runner", font=("Arial", 24, "normal"))
        self.canvas.bye()  # End game

    def start(self, init_dist=400, ai_timer_msec=100):
        """ Start the game """
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)  # Periodically run step function

class ManualMover(turtle.RawTurtle):
    """ Chaser class controlled by keyboard """
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register keyboard events
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass  # No AI logic, manual control

class SmartChaser(turtle.RawTurtle):
    """ Chaser class with AI to catch the runner """
    def __init__(self, canvas, step_move=10):
        super().__init__(canvas)
        self.step_move = step_move

    def run_ai(self, runner_pos, runner_heading):
        """ AI that chases the runner """
        self.setheading(self.towards(runner_pos))  # Set direction towards runner
        self.forward(self.step_move)

class SmartRunner(turtle.RawTurtle):
    """ Runner class that moves strategically to avoid the chaser """
    def __init__(self, canvas, step_move=10, step_turn=10, escape_distance=150):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.escape_distance2 = escape_distance ** 2

    def run_ai(self, chaser_pos, chaser_heading):
        """ Move intelligently to avoid chaser if close """
        p = self.pos()
        q = chaser_pos
        dx, dy = p[0] - q[0], p[1] - q[1]

        # If chaser is within escape distance, move in the opposite direction
        if dx ** 2 + dy ** 2 < self.escape_distance2:
            self.setheading(self.towards(chaser_pos) + 180)  # Move away from chaser
            self.forward(self.step_move)
        else:
            self.forward(self.step_move)
            if random.random() < 0.2:
                self.left(self.step_turn if random.random() < 0.5 else -self.step_turn)

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    runner = SmartRunner(screen)
    chaser = ManualMover(screen)

    # Change shape to default turtle shape and set colors
    runner.shape('turtle')  # Set runner shape to turtle
    runner.color('green')    # Set runner color to green
    chaser.shape('turtle')   # Set chaser shape to turtle
    chaser.color('red')      # Set chaser color to red

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()
