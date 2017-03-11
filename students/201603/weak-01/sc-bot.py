import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine","I am good","Not so bad"]

diaglog = ['What is your name?','what is your name','what is your name?']
diaglog_responses = ['I am steve','steve']

while True:
       userInput = raw_input(">>> ")
       if userInput in greetings:
               random_greeting = random.choice(greetings)
               print(random_greeting)
       elif userInput in diaglog:
               random_greeting = random.choice(diaglog_responses)
               print(random_greeting)
       elif userInput in question:
               random_response = random.choice(responses)
               print(random_response)
       else:
               print("I didn't get what you said")
