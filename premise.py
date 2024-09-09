import json
import os
import glob

def get_user_name():
    valid_names = ["max", "pb", "gen", "drex", "bru", "sha"]
    while True:
        name = input("Please enter your name: ").strip().lower()
        if name in valid_names:
            return name
        else:
            print("Invalid name. Please try again.")

def load_all_premises(folder_paths):
    all_premises = []
    for folder_path in folder_paths:
        for file_path in glob.glob(os.path.join(folder_path, "*_premise.json")):
            with open(file_path, 'r', encoding='utf-8') as f:
                all_premises.extend(json.load(f))
    return all_premises

def main():
    # Corrected JSON string
    input_json = '''
    {
        "url": "https://www.ritemed.com.ph/tamang-kaalaman/acne",
        "premises": [
            {"premise": "Ang pinakamahusay na paraan para mapigilan ito ay ang pagpapabakuna."}
        ]
    }
    '''

    data = json.loads(input_json)

    url = data.get("url", "")
    premises = data.get("premises", [])

    # Prepare the list to store all premises
    output_data_list = []

    # Get the user's name
    user_name = get_user_name()

    # List of folder paths to check for uniqueness
    folder_paths = ["week1/premise", "week2/premise", "week3/premise"]  # Add more folders as needed

    # Create the output file path
    output_file = f"week2/premise/{user_name}_premise.json" # Change the folder every week

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Load all existing premises from the folders
    all_premises = load_all_premises(folder_paths)

    # Extract existing premises for duplicate checking (case insensitive)
    existing_premises = {item["premise"].lower() for item in all_premises}

    # Check if the output file exists and load existing data
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            output_data_list = json.load(f)
        # Determine the next ID
        id_counter = max(item["id"] for item in output_data_list) + 1
    else:
        # Initialize ID counter
        id_counter = 1

    for premise in premises:
        premise_text = premise.get("premise", "")
        if premise_text.lower() not in existing_premises:
            output_data = {
                "id": id_counter,
                "premise": premise_text,
                "url": url,
                "counter": 0
            }
            output_data_list.append(output_data)
            id_counter += 1
            existing_premises.add(premise_text.lower())  # Add to existing premises set

    # Write the updated list to the JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()