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

def combine_json_files(file_paths, output_file):
    combined_data = []

    for file_path in file_paths:
        data = load_json(file_path)
        combined_data.extend(data)

    # Remove duplicates (case insensitive)
    unique_pairs = {}
    for item in combined_data:
        key = (item["hypothesis"].lower(), item["premise"].lower(), item["label"].lower())
        if key not in unique_pairs:
            unique_pairs[key] = item

    # Convert the dictionary back to a list
    combined_unique_data = list(unique_pairs.values())

    save_json(combined_unique_data, output_file)

if __name__ == "__main__":
    file_paths = [
        "week1/week1-augmented.json",
        "week1/week1-hypothesis-pair.json", 
    ]  # Add as many files as needed
    output_file = "week1/combine_hyp-pair.json"
    combine_json_files(file_paths, output_file)