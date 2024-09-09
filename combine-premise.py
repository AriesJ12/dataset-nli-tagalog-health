import json
import os

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def combine_and_move_json_files(file_paths, output_file):
    combined_data = []

    for file_path in file_paths:
        data = load_json(file_path)
        filtered_data = [item for item in data if item["counter"] < 3]
        remaining_data = [item for item in data if item["counter"] >= 3]

        # Save the remaining data back to the original file
        save_json(remaining_data, file_path)

        combined_data.extend(filtered_data)

    # Remove duplicates (case insensitive) and keep the one with the higher counter
    unique_premises = {}
    for item in combined_data:
        premise_lower = item["premise"].lower()
        if premise_lower not in unique_premises:
            unique_premises[premise_lower] = item
        else:
            # If duplicate, keep the one with the higher counter
            if item["counter"] > unique_premises[premise_lower]["counter"]:
                unique_premises[premise_lower] = item

    # Recount IDs
    combined_unique_data = list(unique_premises.values())
    for idx, item in enumerate(combined_unique_data, start=1):
        item["id"] = idx

    save_json(combined_unique_data, output_file)

if __name__ == "__main__":
    week = "week2"
    filenames = ["bru_premise.json", "max_premise.json", "drex_premise.json"]  # Add as many files as needed
    file_paths = [f"{week}/premise/{filename}" for filename in filenames]
    output_file = f"{week}/unfinished_premise.json"
    combine_and_move_json_files(file_paths, output_file)