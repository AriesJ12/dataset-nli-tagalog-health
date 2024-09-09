import json
import os
import random

def get_user_name():
    valid_names = ["max", "pb", "gen", "drex", "bru", "sha"]
    while True:
        name = input("Please enter your name: ").strip().lower()
        if name in valid_names:
            return name
        else:
            print("Invalid name. Please try again.")

def main():
    # Get the user's name
    user_name = get_user_name()

    # Create the output file paths -- change every week
    output_file = f"week2/premise/{user_name}_premise.json"
    hypothesis_file = f"week2/hypothesis/{user_name}_hypothesis-pair.json"
    amount_done = 0

    # Ensure the directories exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    os.makedirs(os.path.dirname(hypothesis_file), exist_ok=True)

    while True:
        print(f"You have done: {amount_done}")
        amount_done += 1

        # Check if the output file exists
        if not os.path.exists(output_file):
            print(f"{output_file} does not exist. Please run the premise script first.")
            return

        # Load existing data
        with open(output_file, 'r', encoding='utf-8') as f:
            premises = json.load(f)

        if not premises:
            print("No premises found in the output file.")
            return

        # Filter premises with counter less than 3
        valid_premises = [p for p in premises if p["counter"] < 3]

        if not valid_premises:
            print("All premises have reached the maximum counter of 3.")
            return

        # Select a random premise
        selected_premise_data = random.choice(valid_premises)
        selected_premise = selected_premise_data["premise"]
        url = selected_premise_data["url"]

        # Randomly choose a question type
        question_types = ["neutral", "contradiction", "entailment"]
        selected_question_type = random.choice(question_types)

        # Prompt the user with the selected premise and question type
        print(f"Premise: {selected_premise}")
        print(f"Question Type: {selected_question_type}")
        hypothesis = input("Please provide a hypothesis: ")

        # Prepare the hypothesis pair data
        hypothesis_pair = {
            "hypothesis": hypothesis,
            "premise": selected_premise,
            "label": selected_question_type,
            "url": url
        }

        # Load existing hypothesis pairs if the file exists
        if os.path.exists(hypothesis_file):
            with open(hypothesis_file, 'r', encoding='utf-8') as f:
                hypothesis_pairs = json.load(f)
        else:
            hypothesis_pairs = []

        # Check for duplicates (case insensitive)
        duplicate_found = any(
            pair["label"].lower() == hypothesis_pair["label"].lower() and
            pair["premise"].lower() == hypothesis_pair["premise"].lower() and
            pair["hypothesis"].lower() == hypothesis_pair["hypothesis"].lower()
            for pair in hypothesis_pairs
        )

        if duplicate_found:
            print("This hypothesis-premise pair already exists. Please try again.")
            continue

        # Append the new hypothesis pair
        hypothesis_pairs.append(hypothesis_pair)

        # Write the updated list to the hypothesis file
        with open(hypothesis_file, 'w', encoding='utf-8') as f:
            json.dump(hypothesis_pairs, f, ensure_ascii=False, indent=4)

        # Update the counter for the selected premise
        for premise in premises:
            if premise["premise"].lower() == selected_premise.lower():
                premise["counter"] += 1
                break

        # Write the updated premises back to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(premises, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()