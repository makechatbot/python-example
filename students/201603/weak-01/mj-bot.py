import turtle as t
import math as m

name = ""

def print_default_lines():
   default_lines = "= * " * 15
   print(default_lines)

def welcome(name):
   print(name + ", Welcome to this AI lecture!")
   print_default_lines()

def welcome_chat(name):
   print(name + ", Welcome to this chat!")
   print_default_lines()

def drawings(color):
   selectedColor = color.upper()
   colors = ('BLUE', 'RED', 'YELLOW')

   if(selectedColor not in colors):
       print("Only Blue, Red, and Yellow are available!")
       return

   t.begin_fill()

   if selectedColor == colors[0]:
       t.color("blue")

   elif selectedColor == colors[1]:
       t.color("red")

   else:
       t.color("yellow")

   for x in range(100):
       h = m.pi * x / 50
       x = 160 * m.sin(h) ** 3
       y = 130 * m.cos(h) - 50 * m.cos(2 * h) - 20 * m.cos(3 * h) - 10 * m.cos(4 * h)
       t.goto(x, y)
   t.end_fill()

def chat():
   print_default_lines()

   while (True):
       text = input(name + " >> ")
       if text == "Hi":
           print("Hi! Welcome to this chat!")
       elif text == "Who are you?":
           print("I am a chat bot!")
       elif text == "How old are you?":
           print("I am 25 years old.")
       elif text == "Telegram is difficult":
           print("너만 어렵냐? 나도 어려워 ㅋㅋㅋㅋㅋ")
       else:
           print("chat-bot>> " + text)

def draw():
   while (True):
       color = input("What color do you like? (Blue, Red, or YELLOW) ")
       if color == "":
           break
       else:
           drawings(str(color))

print_default_lines()
name = input("What is your name? ")
welcome(name)

activity = input("What do you want to do? (Draw? Chat?) ")
selectedActivity = activity.upper()

if selectedActivity == "CHAT":
   chat()
else:
   draw()