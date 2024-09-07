import json
import os

def main():
    # add your text here
    input_json = '''
 {
  "url": "https://mediko.ph/karamdaman/leukemia/",
  "premises": [
    {"premise": "Ang leukemia o lukemya ay isang uri ng kanser na maaring makaapekto sa dugo at sa mga selula na lumilikha ng dugo."},
    {"premise": "Karaniwan itong tinatawag na 'kanser sa dugo' dahil sa paggawa ng bone marrow ng mga abnormal na uri ng white blood cell."},
    {"premise": "Kapag lubhang dumami ang mga abnormal na white blood cell, maaapawan ng mga ito ang mga malulusog na blood cell."},
    {"premise": "Ang mga sintomas ng leukemia ay kinabibilangan ng pagkakaroon ng lagnat, pananamlay, pagdurugo, pagbagsak ng timbang, at labis na pagkakaroon ng impeksyon."},
    {"premise": "Ang leukemia ay maaaring gamutin sa pamamagitan ng operasyon, chemotherapy, radiation, at stem cell transplant."},
    {"premise": "Ang mga uri ng leukemia ay kinabibilangan ng Acute myeloid leukemia (AML), Acute lymphocytic leukemia (ALL), Chronic myeloid leukemia (CML), at Chronic lymphocytic leukemia (CLL)."},
    {"premise": "Wala pang tiyak na sanhi ang leukemia, ngunit ang mga genetic at pangkapaligirang salik ay maaaring magdulot nito."},
    {"premise": "Ang mga salik sa panganib ng leukemia ay kinabibilangan ng kasarian, edad, pagkakaroon nito sa pamilya, at pagkakalantad sa radiation at mga kemikal."},
    {"premise": "Ang mga taong may kanser at kasalukuyang nagpapagamot ay maaaring magkaroon ng leukemia."},
    {"premise": "Ang pagbabago sa pamumuhay at pag-iwas sa ilang uri ng pagkain ay makatutulong upang maiwasan ang leukemia."}
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