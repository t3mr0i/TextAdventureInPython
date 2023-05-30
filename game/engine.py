from game.characters import Character
from api.chat_api import chat_with_gpt3

class GameEngine:
    def __init__(self):
        self.characters = self.create_characters()
        self.current_character = self.characters[0]
         self.map = Map(10, 10)  # Create a 10x10 map
        self.player_position = (0, 0)  # Start the player at the top left corner

    def create_characters(self):
        character_info = {
            "Hero": "You are courageous and resourceful.",
            "Scientist": "You are knowledgeable and inquisitive.",
            "Guide": "You are experienced and wise."
        }

        characters = []
        for name, intro in character_info.items():
            characters.append(Character(name, intro))

        return characters

    def determine_ending(self):
        # Accumulate all characters' ending predictions
        total_predictions = {ending: 0 for ending in FINAL_SEQUENCES}
        for character in self.characters:
            for ending, prediction in character.ending_predictions.items():
                total_predictions[ending] += prediction

        # Add weight to the current character's predictions
        for ending, prediction in self.current_character.ending_predictions.items():
            total_predictions[ending] += prediction

        # Determine the ending with the highest prediction value
        final_ending = max(total_predictions, key=total_predictions.get)
        return final_ending
    

    def chat(self, user_message):
        return self.current_character.chat(user_message)
