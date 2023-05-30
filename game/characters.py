class Character:
    def __init__(self, name, introduction, paths):
        self.name = name
        self.introduction = introduction
        self.paths = paths
        self.memory = []
        self.ending_predictions = {ending: 0 for ending in FINAL_SEQUENCES}

    def chat(self, user_message):
        messages = [
            {"role": "system", "content": f"You are {self.name}. {self.introduction}."},
            {"role": "user", "content": user_message},
        ]
        messages.extend(self.memory)

        # Update ending predictions based on user_message
        for ending, keywords in self.paths.items():
            for keyword in keywords:
                if keyword in user_message:
                    self.ending_predictions[ending] += 1

        response = chat_with_gpt3(messages)

        # Save the conversation to the character's memory
        self.memory.append({"role": "assistant", "content": response})
        save_character_memory(self.name, self.memory)

        return response
