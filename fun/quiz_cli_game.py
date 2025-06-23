import json
import random

def load_questions(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f" Failed to load questions: {e}")
        return []

def run_quiz(questions):
    print("\n Quiz Time!")
    print("-" * 30)
    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        options = q['options']
        random.shuffle(options)

        for i, opt in enumerate(options):
            print(f"  {i + 1}. {opt}")

        try:
            choice = int(input("Your answer (1-4): "))
            if options[choice - 1] == q['answer']:
                print(" Correct!")
                score += 1
            else:
                print(f" Wrong. Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print(f"Invalid input. Correct answer: {q['answer']}")

    print("\n Quiz Finished!")
    print(f"Your Score: {score} / {len(questions)}")

def main():
    filename = "questions.json"
    questions = load_questions(filename)
    if questions:
        run_quiz(questions)
    else:
        print(" No questions available to run quiz.")

if __name__ == "__main__":
    main()
