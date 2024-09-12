import json
import random
import os

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_subset(data, percentage=None, number=None):
    if percentage is not None:
        subset_size = int(len(data) * (percentage / 100))
    elif number is not None:
        subset_size = number
    else:
        raise ValueError("Either percentage or number must be specified.")
    
    subset = random.sample(data, subset_size)
    return subset

def divide_file(input_file, output_dir, num_files):
    data = load_json(input_file)
    random.shuffle(data)
    chunk_size = len(data) // num_files
    for i in range(num_files):
        chunk = data[i * chunk_size:(i + 1) * chunk_size]
        output_file = os.path.join(output_dir, f"subset_{i + 1}.json")
        save_json(chunk, output_file)
    
    # Save the remaining data back to the input file
    remaining_data = data[num_files * chunk_size:]
    save_json(remaining_data, input_file)

def extract_multiple_subsets(input_file, output_dir, number, times):
    data = load_json(input_file)
    for i in range(times):
        subset = get_subset(data, number=number)
        remaining_data = [item for item in data if item not in subset]
        output_file = os.path.join(output_dir, f"subset_{i + 1}.json")
        save_json(subset, output_file)
        data = remaining_data
    
    # Save the remaining data back to the input file
    save_json(data, input_file)

def main():
    input_file = "week1/combine_hyp-pair.json"
    output_dir = "week1/subsets"
    os.makedirs(output_dir, exist_ok=True)

    # Example usage for dividing a file into 10 smaller files
    # divide_file(input_file, output_dir, num_files=2)

    # Example usage for extracting 100 items from a file, 5 times
    extract_multiple_subsets(input_file, output_dir, number=100, times=5)

if __name__ == "__main__":
    main()