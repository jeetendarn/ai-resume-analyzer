
import json
import csv
import tempfile

def export_json(data):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")

    with open(temp.name, "w") as f:
        json.dump(data, f, indent=4)

    return temp.name

def export_csv(data):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")

    with open(temp.name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Field", "Value"])

        for key, value in data.items():
            writer.writerow([key, str(value)])

    return temp.name
