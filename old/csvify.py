import csv
import json

import pandas as pd


def flatten_json(y):
    out = {}

    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + ".")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + ".")
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Read the JSON file
with open("filtered_sarcoma_studies.json", "r") as file:
    studies = json.load(file)

# Flatten each study
flattened_studies = [flatten_json(study) for study in studies]

# Convert to DataFrame
df = pd.DataFrame(flattened_studies)

# Save to CSV
df.to_csv("all_sarcoma_studies_info.csv", index=False)

print("CSV file 'all_sarcoma_studies_info.csv' has been created.")
