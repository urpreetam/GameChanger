from datetime import datetime
class GameState:
    def __init__(self, character=None, box_id=None, choices=None, story_progress="", start_time=None):
        self.character = character
        self.box_id = box_id
        self.choices = choices if choices is not None else []
        self.story_progress = story_progress if story_progress else "You wake up in a dark forest. What do you do?"
        self.start_time = start_time if start_time else datetime.now()

    def add_choice(self, choice):
        self.choices.append(choice)

    def update_story(self, new_story):
        self.story_progress += new_story + "\n"

    def get_current_state(self):
        return {
            "character": self.character,
            "box_id": self.box_id,
            "choices": self.choices,
            "story_progress": self.story_progress
        }
