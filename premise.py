import json
import os

def main():
    # add your text here
    input_json = '''
  {
  "url": "https://www.chcrr.org/tl/health-topic/leukemia/#:~:text=Ano%20ang%20leukemia%3F,ng%20dugo%2C%20at%20mga%20platelet.",
  "premises": [
    {"premise": "Ang leukemia ay isang kanser ng mga selula ng dugo na nagsisimula sa mga tissue na bumubuo ng dugo tulad ng bone marrow."},
    {"premise": "Ang bone marrow ay gumagawa ng mga selula na bubuo sa mga puting selula ng dugo, pulang selula ng dugo, at mga platelet."},
    {"premise": "Ang mga puting selula ng dugo ay tumutulong sa katawan na labanan ang impeksiyon, ang mga pulang selula ng dugo ay naghahatid ng oxygen, at ang mga platelet ay tumutulong sa pagbuo ng mga clots upang ihinto ang pagdurugo."},
    {"premise": "Sa leukemia, ang bone marrow ay gumagawa ng malaking bilang ng mga abnormal na selula na namumuo sa bone marrow at dugo, na nagpapahirap sa malusog na mga selula ng dugo na gawin ang kanilang trabaho."},
    {"premise": "May iba't ibang uri ng leukemia na nakadepende sa uri ng selula ng dugo na nagiging kanser at kung ito ay mabilis o mabagal na lumalaki."},
    {"premise": "Ang pangunahing uri ng leukemia ay kinabibilangan ng Talamak na lymphocytic leukemia (ALL), Talamak na myeloid leukemia (AML), Talamak na lymphocytic leukemia (CLL), at Talamak na myeloid leukemia (CML)."},
    {"premise": "Ang leukemia ay nangyayari kapag may mga pagbabago sa genetic material (DNA) sa bone marrow cells, ngunit ang sanhi ng mga pagbabagong ito ay hindi alam."},
    {"premise": "Ang mga sintomas ng leukemia ay maaaring kabilang ang pagkapagod, lagnat o pagpapawis sa gabi, madaling pagdurugo o pag-bruising, pagbaba ng timbang, at petechiae."},
    {"premise": "Ang diagnosis ng leukemia ay maaaring gamitin ang mga tool tulad ng pisikal na pagsusulit, medikal na kasaysayan, pagsusuri sa dugo, pagsusuri sa utak ng buto, at mga pagsusuri sa genetika."},
    {"premise": "Ang mga paggamot para sa leukemia ay maaaring kabilang ang kimoterapya, therapy radiation, chemotherapy na may pag-transplant ng stem cell, at naka-target na therapy."}
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