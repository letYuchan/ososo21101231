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
        self.points = 0  # Initial score

        # Instantiate a turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        # Background setup
        self.canvas.bgcolor("yellow")  # Change background color to yellow

        # Save score and timer text
        self.score_text = self.drawer.clone()  # Clone turtle for score text
        self.timer_text = self.drawer.clone()  # Clone turtle for timer text
        self.caught_text = self.drawer.clone()  # Clone turtle for state text

        self.score_text.setpos(-300, 300)  # Set score position
        self.timer_text.setpos(-300, 250)  # Set timer position
        self.caught_text.setpos(-300, 220)  # Set state text position

    def is_caught(self):
        """ Check if the runner is caught by the chaser """
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx ** 2 + dy ** 2 < self.catch_radius2

    def update_timer(self):
        """ Update elapsed time and display it """
        elapsed_time = time.time() - self.start_time
        self.timer_text.clear()  # Clear previous timer text
        self.timer_text.write(f'Timer: {elapsed_time:.2f}s', move=False)

        # End game after 60 seconds
        if elapsed_time > 60:  # After 60 seconds
            self.finish_game(won=False)

    def update_points(self):
        """ Update points; increase if the runner is not caught """
        if not self.is_caught():
            self.points += 1
        return self.points

    def step(self):
        """ Move runner and chaser in each game step """
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        # Chaser is controlled manually, so no AI logic here

        caught = self.is_caught()

        # Clear previous score and state text
        self.score_text.clear()
        self.caught_text.clear()

        # Display updated points and caught status
        self.score_text.write(f'Points: {self.update_points()}', font=("Arial", 16, "normal"))

        # Check if caught and display appropriate message
        if caught:
            self.caught_text.write(f'Caught status: True', font=("Arial", 16, "normal"))
            self.finish_game(won=True)  # Finish the game if caught
        else:
            self.caught_text.write(f'Caught status: False', font=("Arial", 16, "normal"))

        # Update timer
        self.update_timer()

        # Keep the game running
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def finish_game(self, won):
        """ Handle game over condition """
        self.drawer.setpos(-200, 0)
        if won:
            self.drawer.write("Runner was caught!", font=("Arial", 24, "normal"))
        else:
            self.drawer.write("Runner escaped!", font=("Arial", 22, "bold"))
        self.canvas.bye()  # Close the game window

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

class RandomMover(turtle.RawTurtle):
    """ Runner class that moves randomly with improved AI """
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.shape('turtle')  # Set runner shape to turtle
        self.color('red')  # Change runner color to red

    def run_ai(self, opp_pos, opp_heading):
        """ Intelligent movement to escape the chaser """
        # Calculate the distance to the chaser
        distance_to_chaser = self.distance(opp_pos)

        # If the chaser is close, move in the opposite direction
        if distance_to_chaser < 150:  # Adjust distance threshold as needed
            self.setheading(self.towards(opp_pos) + 180)  # Move away from chaser
            self.forward(self.step_move)
        else:
            # Random movement if the chaser is far away
            mode = random.randint(0, 2)
            if mode == 0:
                self.forward(self.step_move)
            elif mode == 1:
                self.left(self.step_turn)
            elif mode == 2:
                self.right(self.step_turn)

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # Create the runner (AI) and chaser (manual control)
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()
