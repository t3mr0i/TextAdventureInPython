from game.engine import GameEngine

game = GameEngine()

while True:
    user_message = input("> ")
    if user_message.lower() == "quit":
        break
    else:
        response = game.chat(user_message)
        print(response)
