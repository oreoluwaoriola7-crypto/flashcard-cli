class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.times_correct = 0
        self.times_wrong = 0

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "times_correct": self.times_correct,
            "times_wrong": self.times_wrong
        }

    @classmethod
    def from_dict(cls, data):
        card = cls(data["question"], data["answer"])
        card.times_correct = data["times_correct"]
        card.times_wrong = data["times_wrong"]
        return card

    def __str__(self):
        return f"Q: {self.question} | A: {self.answer}"