from deck import Deck
from session import StudySession

def show_menu():
    print("\n--- Flashcard CLI ---")
    print("1. Add a card")
    print("2. Study")
    print("3. View all cards")
    print("4. Quit")

def main():
    deck = Deck("Python Basics")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            question = input("Enter question: ").strip()
            answer = input("Enter answer: ").strip()
            deck.add_card(question, answer)
            print("Card added!")

        elif choice == "2":
            session = StudySession(deck)
            session.start()

        elif choice == "3":
            if len(deck.cards) == 0:
                print("No cards yet.")
            else:
                print(f"\n{deck}")
                for i, card in enumerate(deck.cards, 1):
                    print(f"{i}. {card}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()