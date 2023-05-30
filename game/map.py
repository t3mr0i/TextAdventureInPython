class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['?' for _ in range(width)] for _ in range(height)]
        self.npcs = self.populate_npcs()
        self.items = self.populate_items()

    def populate_npcs(self):
        npcs = {}
        for npc in self.npcs:
            x, y = self.get_random_position()
            npcs[(x, y)] = npc
        return npcs

    def populate_items(self):
        items = {}
        for item in self.items:
            x, y = self.get_random_position()
            items[(x, y)] = item
        return items

    def get_random_position(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        return x, y

    def update_map(self, player_position):
        x, y = player_position
        self.grid[y][x] = 'P'  # Indicate player's position
        if player_position in self.npcs:
            self.grid[y][x] = 'N'  # Indicate NPC's position
        if player_position in self.items:
            self.grid[y][x] = 'I'  # Indicate item's position

    def draw_map(self):
        for row in self.grid:
            print(' '.join(row))

# Now, you'll need to add a `map` property to the `GameEngine` class,
# and update it whenever the player moves.

class GameEngine:
    # ...
    

    def process_input(self, user_input):
        # Update player's position based on user_input
        # For simplicity, let's assume the player can only move right
        if user_input == "move right":
            self.player_position = (self.player_position[0]+1, self.player_position[1])
            self.map.update_map(self.player_position)

    def print_map(self):
        self.map.draw_map()
