import random

class StudySession:
    def __init__(self, deck):
        self.deck = deck
        self.score = 0
        self.total = 0

    def start(self):
        if len(self.deck.cards) == 0:
            print("No cards in deck. Add some cards first!")
            return

        cards = random.sample(self.deck.cards, len(self.deck.cards))

        print(f"\nStarting session: {len(cards)} cards\n")

        for card in cards:
            print(f"Question: {card.question}")
            user_answer = input("Your answer: ").strip().lower()
            correct_answer = card.answer.strip().lower()

            if user_answer == correct_answer:
                print("Correct!\n")
                card.times_correct += 1
                self.score += 1
            else:
                print(f"Wrong! The answer was: {card.answer}\n")
                card.times_wrong += 1

            self.total += 1

        self.deck.save()
        self.show_result()

    def show_result(self):
        print(f"Session complete! Score: {self.score}/{self.total}")