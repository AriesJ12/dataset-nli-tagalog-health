import json
import os

def main():
    # add your text here
    input_json = '''
{
  "url": "https://www.ritemed.com.ph/malaria/malaria-101-sanhi-sintomas-at-lunas-sa-sakit",
  "premises": [
    {"premise": "Ang malaria ay isang malubhang sakit na maaaring humantong sa kasawian ng nag-contract nito."},
    {"premise": "Isang parasite ang sanhi ng pagiging carrier ng isang lamok ng malaria."},
    {"premise": "Ang mga pangkaraniwang sintomas ng malaria ay mataas na lagnat, panginginig ng katawan, at mala-trangkasong pakiramdam sa katawan."},
    {"premise": "May apat na uri ng malaria parasites na nanghahawa sa mga tao: Plasmodium falciparum, P. vivax, P. ovale, at P. malariae."},
    {"premise": "Sa Pilipinas at ibang bansa sa Southeast Asia, may P. knowlesi rin na uri ng malaria na hinahawahan ang ilang macaques na kayang makapanghawa ng tao (zoonotic malaria)."},
    {"premise": "Ang P. falciparum ang madalas na nagdudulot ng malalang infection na humahantong sa kasawian kapag hindi naagapan at nagamot nang maaga."},
    {"premise": "Ang malaria ay nagkakaroon dahil sa mosquito bites mula sa isang infected female na lamok o Anopheles mosquito."},
    {"premise": "Ang malaria parasites ay makikita sa red blood cells ng isang taong mayroon nang malaria at maaari ring malipat sa pamamagitan ng blood transfusion, organ transplant, o unhygienic na paggamit ng mga karayom at syringes."},
    {"premise": "Maaari ring malipat ang malaria mula sa isang nagbubuntis tungo sa pinagbubuntis nito bago o habang nanganganak."},
    {"premise": "Karamihan ng nagkakasakit ng malaria ay makararamdam ng mataas na lagnat, pagpapawis pero panlalamig, pananakit ng mga masel, pagkahilo, at pagsusuka."},
    {"premise": "Ang pinakamainam na solusyon upang malaman kung may malaria ang isang tao ay pagsangguni sa medical experts at pagkuha ng diagnostic test."},
    {"premise": "Ang malaria na dulot ng P. vivax at P. ovale ay may malaking tiyansa na mag-relapse sa isang gumaling na pasyente dahil sa pagiging dormant ng mga parasite sa atay."},
    {"premise": "Maraming gamot ang available para maagapan ang pagkakaroon ng malaria; inirerekomenda ng Centers for Disease Control and Prevention (CDC) ang mga bansang may mataas na kaso ng malaria transmission at mga epektibong gamot para sa bawat lugar."},
    {"premise": "Wala pang available na malaria vaccine, ngunit tuloy pa rin ang clinical trials para makapaglabas ng bakuna kontra sa malaria."}
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