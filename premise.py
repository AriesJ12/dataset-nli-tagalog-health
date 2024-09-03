import json
import os

def main():
    # add your text here
    input_json = '''
  {
  "url": "https://www.chcrr.org/tl/health-topic/flu/",
  "premises": [
    {"premise": "Ang trangkaso, na tinatawag ding influenza, ay isang impeksyon sa paghinga na dulot ng mga virus."},
    {"premise": "Ang trangkaso ay sanhi ng mga virus ng trangkaso na kumakalat mula sa tao patungo sa tao."},
    {"premise": "Ang mga sintomas ng trangkaso ay biglang dumarating at maaaring kabilang ang lagnat o nakakaramdam ng lagnat/panginginig, ubo, namamagang lalamunan, makinis o madulas na ilong, sakit sa kalamnan o katawan, pananakit ng ulo, at pagod."},
    {"premise": "Ang trangkaso ay maaari ring magpalala ng mga malalang problema sa kalusugan tulad ng hika, diabetes, at sakit sa puso."},
    {"premise": "Upang masuri ang trangkaso, gagawa muna ng medikal na kasaysayan ang mga tagapagbigay ng pangangalagang pangkalusugan at magtatanong tungkol sa iyong mga sintomas."},
    {"premise": "Karamihan sa mga taong may trangkaso ay gumagaling sa kanilang sarili nang walang pangangalagang medikal, ngunit maaaring kailanganin ang mga gamot na antiviral upang gamutin ang trangkaso."},
    {"premise": "Ang pinakamahusay na paraan upang maiwasan ang trangkaso ay ang makakuha ng bakuna laban sa trangkaso taon-taon."}
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