import json
import os

def main():
    # add your text here
    input_json = '''
 {
  "url": "https://fil.hesperian.org/hhg/Where_Women_Have_No_Doctor:Ano_ang_HIV_at_AIDS%3F",
  "premises": [
    {"premise": "Ang HIV (Human Immunodeficiency Virus) ay isang napakaliit na mikrobyo na hindi nakikita ng mata."},
    {"premise": "Ang AIDS (Acquired Immune Deficiency Syndrome) ay namumuo sa kalaunan pagkatapos maimpeksyon ng HIV."},
    {"premise": "Kapag naimpeksyon ng HIV, inaatake ng virus ang immune system at unti-unting pinapatay ang mga selyula nito."},
    {"premise": "Karamihan sa mga taong may HIV ay hindi nagkakasakit mula sa virus nang 5–10 taon, ngunit sa kalaunan ay hindi na nila kayang labanan ang karaniwang mga impeksyon."},
    {"premise": "Ang HIV ay maaaring ipasa sa iba kahit na ang taong may impeksyon ay malusog ang pakiramdam."},
    {"premise": "Ang HIV ay naipapasa sa pamamagitan ng mga likido ng katawan tulad ng dugo, tamod, at likido sa loob ng puwerta."},
    {"premise": "Ang HIV ay hindi naipapasa sa pamamagitan ng paghahawak, paghalik, pagyakap, pagsalo sa pagkain, pagsalo sa higaan, o paghihiraman ng damit."},
    {"premise": "Ang mga taong may AIDS ay may huminang immune system at maaaring magkaruon ng mga bihirang impeksyon o kanser."},
    {"premise": "Makakatulong ang mahusay na nutrisyon at ilang gamot para malabanan ang mga impeksyong dulot ng AIDS at mapahaba ang buhay, ngunit walang nagpapagaling sa AIDS mismo."}
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