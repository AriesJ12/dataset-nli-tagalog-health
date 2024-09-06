import json
import os

def main():
    # add your text here
    input_json = '''
{
  "url": "https://vlmakabalihospital.com.ph/ano-ang-dahilan-ng-psoriasis/",
  "premises": [
    {"premise": "Ang Psoriasis ay isang sakit kung saan mabilis na mabuo ang mga cells sa ibabaw ng balat."},
    {"premise": "Ang psoriasis ay bumubuo at kumakapal ang balat na parang kaliskis, tuyong patse-patse, kulay pula at makati."},
    {"premise": "Ang mga kaliskis ng psoriasis ay gaya ng makakapal na balakubak at sumisingaw sa ibang parte ng iyong katawan tulad ng tuhod, siko, tadyang at anit."},
    {"premise": "Ang psoriasis ay hindi nakahahawa at hindi maikalat sa ibang tao sa pamamagitan ng paghawak at pagdikit sa balat."},
    {"premise": "Ang mga bagay na maaaring makapagpalala ng psoriasis ay ang impeksyon, pinsala sa balat, stress, malamig na panahon at paninigarilyo."}
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