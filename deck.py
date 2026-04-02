import json
import os
from card import Card

class Deck:
    def __init__(self, name, filepath="data/cards.json"):
        self.name = name
        self.filepath = filepath
        self.cards = []
        self.load()

    def add_card(self, question, answer):
        card = Card(question, answer)
        self.cards.append(card)
        self.save()

    def save(self):
        data = {
            "name": self.name,
            "cards": [card.to_dict() for card in self.cards]
        }
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.name = data["name"]
                self.cards = [Card.from_dict(c) for c in data["cards"]]

    def __str__(self):
        return f"Deck: {self.name} | {len(self.cards)} cards"