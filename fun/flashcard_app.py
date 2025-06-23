import json
import random

def load_flashcards(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f" Could not load flashcards: {e}")
        return []

def run_flashcards(cards):
    print("\n Flashcard Learning Mode")
    print("-" * 30)
    random.shuffle(cards)
    
    for i, card in enumerate(cards, 1):
        print(f"\nCard {i}: {card['question']}")
        input(" Press Enter to flip...")
        print(f" Answer: {card['answer']}")
        input("  Press Enter for next...")

    print("\n All flashcards reviewed!")

def main():
    filename = "flashcards.json"
    cards = load_flashcards(filename)
    if cards:
        run_flashcards(cards)
    else:
        print(" No flashcards to display.")

if __name__ == "__main__":
    main()
