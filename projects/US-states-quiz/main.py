import turtle
import pandas
# initializing the screen
game_screen = turtle.Screen()
game_screen.title("US States game")
game_screen.listen()
# first exit mechnism
game_screen.onkey(fun=game_screen.bye, key='Escape')
# background setup
image = "blank_states_img.gif"
game_screen.addshape(image)
# make the image available to be used by the turtle
turtle.shape(image)

states_dataframe = pandas.read_csv("50_states.csv")
states_list = states_dataframe.state.to_list()
STATES_NUMBER = 50

class Writer(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(15)
        self.speed(0)
        self.hideturtle()
        self.correct_answers = 0
        self.taken = []
    def put_word(self, word, x, y):
        ''' string to be written & x, y coords'''
        self.taken.append(s)
        self.goto(x, y)
        self.write(word)
    def increase_score(self):
        self.correct_answers += 1
    def goodbye(self):
        # generate csv file of misses
        missed = states_list
        for state in missed:
            if state in self.taken:
                missed.remove(state)
        df = pandas.DataFrame(missed)
        df.to_csv("missed.csv")
        print("Game ended successfully")
        print("A csv file containing the missed states was generated")

judge = Writer()

while judge.correct_answers < STATES_NUMBER:
    s = str(game_screen.textinput(title=f"{judge.correct_answers}/{STATES_NUMBER} correct",
                                  prompt="Enter the name of a state"))
    s = s.title()
    if (s == "Exit"):
        break
        
    if states_list.count(s) != 0:
        if judge.taken.count(s) == 0:
            print('bravo')
            mystate = states_dataframe[states_dataframe.state == s]
            xcoor = mystate.x.item() # .item() solves a lot of problems
            ycoor = mystate.y.item()
            judge.put_word(s, xcoor, ycoor)
            judge.increase_score()
    else:
        print("does not exist")

judge.goodbye()