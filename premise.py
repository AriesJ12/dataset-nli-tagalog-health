import json
import os

def main():
    # add your text here
    input_json = '''
{
  "url": "https://www.chcrr.org/tl/health-topic/chikungunya/#:~:text=Ang%20Chikungunya%20ay%20isang%20virus,sa%20pamamagitan%20ng%20nahawaang%20dugo.",
  "premises": [
    {"premise": "Ang Chikungunya ay isang virus na kumakalat ng parehong mga uri ng lamok na kumakalat dengge at Zika virus."},
    {"premise": "Karamihan sa mga taong nahawaan ng Chikungunya ay magkakaroon ng mga sintomas, na maaaring malubha."},
    {"premise": "Ang pinakakaraniwang sintomas ng Chikungunya ay lagnat at pananakit ng kasukasuan."},
    {"premise": "Ang mga taong nasa panganib para sa mas malubhang sakit mula sa Chikungunya ay kinabibilangan ng mga bagong silang, matatanda, at mga taong may mga sakit gaya ng altapresyon, diabetes, o sakit sa puso."},
    {"premise": "Maaaring ipakita ng pagsusuri sa dugo kung mayroon kang Chikungunya virus."},
    {"premise": "Walang bakuna o gamot para sa Chikungunya, ngunit maaaring makatulong ang pag-inom ng maraming likido, pagpapahinga, at pag-inom ng mga non-aspirin pain reliever."}
  ]
}




    '''

    data = json.loads(input_json)

    url = data.get("url", "")
    premises = data.get("premises", [])

    # Prepare the list to store all premises
    output_data_list = []

    output_file = "output.json"

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