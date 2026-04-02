# Flashcard CLI

A command-line flashcard app built with Python. Create decks, add cards, and test yourself — all from the terminal.

## Features

- Add flashcards with a question and answer
- Study your deck in random order
- Track correct and wrong answers per card
- Cards saved automatically to a JSON file

## Project Structure
```
flashcard-cli/
├── main.py        # Entry point and CLI menu
├── card.py        # Card class
├── deck.py        # Deck class with JSON load/save
├── session.py     # StudySession class
├── data/
│   └── cards.json # Saved flashcards
```

## How to Run
```bash
python main.py
```

## Built With

- Python 3
- OOP (classes and objects)
- JSON for data storage

## Author

Oreoluwa — aspiring data scientist