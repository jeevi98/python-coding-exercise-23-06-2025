import time
import random


texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a useful skill for everyone to learn.",
    "Practice makes perfect, especially when typing fast.",
    "Python is a versatile programming language."
]

def calculate_wpm(start_time, end_time, text):
    time_taken = end_time - start_time
    words = len(text.split())
    wpm = (words / time_taken) * 60
    return wpm

def calculate_accuracy(original, typed):
    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    total_chars = len(original)
    accuracy = (correct_chars / total_chars) * 100
    return accuracy

def main():
    print(" Typing Speed Test")
    print("-" * 30)
    test_text = random.choice(texts)
    print(f"\n Type the following:\n\n{test_text}\n")
    input(" Press Enter when you're ready...")

    start_time = time.time()
    typed_text = input("\n You: ")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, test_text)
    accuracy = calculate_accuracy(test_text, typed_text)

    print("\n Results")
    print("-" * 30)
    print(f"Time Taken: {end_time - start_time:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
