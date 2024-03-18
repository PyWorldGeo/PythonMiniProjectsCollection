import json
from difflib import get_close_matches

def load_database(file_path):
    """
    Reads data from JSON file
    :param file_path: The path to JSON File
    :return: A Dictionary of the JSON Data
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def save_database(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def find_match(user_question, questions):
    matches = get_close_matches(user_question, questions, cutoff=0.6, n=1)
    return matches[0] if matches else None

def get_answer(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    data_base = load_database("database.json")

    while True:
        user_input = input('You: ').lower()

        if user_input.lower() == 'quit':
            break

        best_match = find_match(user_input, [q["question"] for q in data_base["questions"]])

        if best_match:
            answer = get_answer(best_match, data_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input("Type the answer or 'skip' to skip:")

            if new_answer.lower() != "skip":
                data_base["questions"].append({"question": user_input, "answer": new_answer})
                save_database('database.json', data_base)
                print("Bot: Thank You! I learned a new response!")


chat_bot()