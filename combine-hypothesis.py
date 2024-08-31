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
    unique_pairs = {}
    for item in combined_data:
        key = (item["hypothesis"].lower(), item["premise"].lower(), item["label"].lower())
        if key not in unique_pairs:
            unique_pairs[key] = item

    # Convert the dictionary back to a list
    combined_unique_data = list(unique_pairs.values())

    save_json(combined_unique_data, output_file)

if __name__ == "__main__":
    #CHANGE HERE
    file1 = "file1.json"
    file2 = "file2.json"
    output_file = "final_hypothesis-pair.json"
    combine_json_files(file1, file2, output_file)