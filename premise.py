import json
import os

def get_user_name():
    valid_names = ["max", "pb", "gen", "drex", "bru", "sha"]
    while True:
        name = input("Please enter your name: ").strip().lower()
        if name in valid_names:
            return name
        else:
            print("Invalid name. Please try again.")

def main():
    # add your text here
    input_json = '''
{
  "url": "https://www.chcrr.org/tl/health-topic/tetanus/#:~:text=Buod,o%20sa%20pamamagitan%20ng%20paso.",
  "premises": [
    {"premise": "Ang Tetanus ay isang malubhang sakit na dulot ng Clostridium bacteria."},
    {"premise": "Ang bakterya na sanhi ng tetanus ay nabubuhay sa lupa, laway, alikabok, at dumi."},
    {"premise": "Ang bakterya ng tetanus ay maaaring makapasok sa katawan sa pamamagitan ng malalim na hiwa o paso."},
    {"premise": "Ang impeksyon ng tetanus ay nagdudulot ng masakit na paninikip ng mga kalamnan at maaaring humantong sa 'pag-lock' ng panga."},
    {"premise": "Ang tetanus ay isang medikal na emerhensiya at kailangan ng agarang pangangalaga sa ospital."},
    {"premise": "Maaari mong maiwasan ang tetanus sa pamamagitan ng pagbabakuna, na ibinibigay bilang bahagi ng karaniwan na pagbabakuna sa pagkabata."},
    {"premise": "Ang mga nasa hustong gulang ay dapat magpakuha ng tetanus booster shot tuwing 10 taon at kung magkakaroon ng masamang hiwa o paso."}
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

    # Create the output file path
    output_file = f"week2/premise/{user_name}_premise.json"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Check if the output file exists
    if os.path.exists(output_file):
        # Load existing data
        with open(output_file, 'r', encoding='utf-8') as f:
            output_data_list = json.load(f)
        # Determine the next ID
        id_counter = max(item["id"] for item in output_data_list) + 1
    else:
        # Initialize ID counter
        id_counter = 1

    # Extract existing premises for duplicate checking (case insensitive)
    existing_premises = {item["premise"].lower() for item in output_data_list}

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