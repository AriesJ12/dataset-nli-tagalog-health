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
  "url": "https://www.vdh.virginia.gov/content/uploads/sites/3/2023/05/Tagalog-COVID_19_Fact_Sheet_2023_508c.pdf",
  "premises": [
    {"premise": "Ang Coronavirus Disease 2019, na karaniwang kilala bilang COVID-19, ay isang respiratoryong impeksyon na dulot ng Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2)."},
    {"premise": "Ang COVID-19 ay labis na nakakahawa at maaaring magresulta sa pagkakasakit sa mga taong walang immunity mula sa pagbabakuna o kamakailang pagkakasakit."},
    {"premise": "Ang mga matatanda at mga taong may malubhang karamdaman tulad ng sakit sa puso o baga, at diyabetis, ay nasa mas mataas na peligro para sa malalang COVID-19 na pagkakasakit."},
    {"premise": "Kumakalat ang COVID-19 kapag ang taong nahawahan ay nagbubuga ng hininga na may kasamang droplet o maliliit na particle na naglalaman ng virus, na maaaring malanghap ng ibang tao."},
    {"premise": "Kasama sa mga sintomas ng COVID-19 ang lagnat, ubo, kahirapan sa paghinga, pagkapagod, pananakit ng katawan, pagkawala ng panlasa o pang-amoy, at iba pa."},
    {"premise": "Ang mga matatanda at may malubhang karamdaman ay may mas mataas na peligro na magkaroon ng malalang COVID-19, na maaaring magdulot ng hirap sa paghinga, pananakit ng dibdib, at pagkamatay."},
    {"premise": "Dalawang klase ng viral test ang ginagamit para ma-diagnose ang COVID-19: molecular test (RT-PCR) at antigen test."},
    {"premise": "Ang pagbabakuna ay isang mahalagang estratehiya para mapabagal ang pagkalat ng COVID-19, lalo na sa mga matatanda at mga may umiiral na kondisyong medikal."}
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