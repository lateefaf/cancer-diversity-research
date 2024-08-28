import json


def has_race_nih_omb(study):
    try:
        baseline_characteristics = study["resultsSection"][
            "baselineCharacteristicsModule"
        ]
        measures = baseline_characteristics.get("measures", [])
        return any(measure.get("title") == "Race (NIH/OMB)" for measure in measures)
    except KeyError:
        return False


matching_studies = []

# Read the file and process each line
with open("cancer_studies.json", "r") as file:
    # Read all lines and join them, then surround with brackets to make it a valid JSON array
    data = "[" + "".join(file.readlines()).rstrip(",") + "]"

    # Parse the JSON data
    studies = json.loads(data)

    for study in studies:
        if has_race_nih_omb(study):
            matching_studies.append(study)

print(f"Found {len(matching_studies)} studies with 'Race (NIH/OMB)' measure.")

# Save matching studies to a new JSON file
with open("filtered_sarcoma_studies.json", "w") as file:
    json.dump(matching_studies, file, indent=2)

print("Matching studies have been saved to 'filtered_sarcoma_studies.json'")
