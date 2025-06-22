
def simple_quiz_game():
    # List of questions and answers
    questions = [
        {"question": "What is the sum of  2 + 2?", "answer": "4"},
        {"question": "What color is the sky?", "answer": "blue"},
        {"question": "What is the capital of Ethiopia?", "answer": "Addis Ababa"},
        {"question": "What is the difference 5 - 3?", "answer": "2"},
        {"question": "What is the largest planet?", "answer": "Jupiter"}
    ]

    score = 0
    incorrect_answers = []

    # Ask each question
    for q in questions:
        user_answer = input(q["question"] + " ").strip().lower()
        if user_answer == q["answer"].lower():
            score += 1
        else:
            incorrect_answers.append((q["question"], q["answer"]))

    # Display score
    total_questions = len(questions)
    print(f"\nYour score: {score}/{total_questions}")

    # Display correct answers for incorrect questions
    if incorrect_answers:
        print("\nYou got these questions wrong:")
        for question, correct_answer in incorrect_answers:
            print(f"- {question} (Correct answer: {correct_answer})")
    else:
        print("Awesome! You got all questions right!")

simple_quiz_game()