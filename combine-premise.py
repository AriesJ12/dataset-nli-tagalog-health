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

def combine_json_files(file1, file2, output_file):
    data1 = load_json(file1)
    data2 = load_json(file2)

    combined_data = data1 + data2

    # Remove duplicates (case insensitive)
    unique_premises = {}
    for item in combined_data:
        premise_lower = item["premise"].lower()
        if premise_lower not in unique_premises:
            unique_premises[premise_lower] = item

    # Recount IDs
    combined_unique_data = list(unique_premises.values())
    for idx, item in enumerate(combined_unique_data, start=1):
        item["id"] = idx

    save_json(combined_unique_data, output_file)

if __name__ == "__main__":
    # CHANGE HERE
    file1 = "file1.json"
    file2 = "file2.json"
    output_file = "final_premise.json"
    combine_json_files(file1, file2, output_file)