import json
import os
import math

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def divide_json_file(input_file, output_prefix, num_files):
    data = load_json(input_file)

    # Filter data with counter less than 3
    filtered_data = [item for item in data if item["counter"] < 3]

    # Ensure the number of files is within the valid range
    num_files = min(max(3, num_files), 6)

    # Split the data into chunks
    chunk_size = math.ceil(len(filtered_data) / num_files)
    chunks = [filtered_data[i:i + chunk_size] for i in range(0, len(filtered_data), chunk_size)]

    # Save each chunk to a separate file
    for i, chunk in enumerate(chunks):
        output_file = f"{output_prefix}_{i + 1}.json"
        save_json(chunk, output_file)
        print(f"Saved {len(chunk)} items to {output_file}")

if __name__ == "__main__":
    input_file = "week1-final_premise.json"
    output_prefix = "output"
    num_files = 4  # Change this value to the desired number of output files
    divide_json_file(input_file, output_prefix, num_files)