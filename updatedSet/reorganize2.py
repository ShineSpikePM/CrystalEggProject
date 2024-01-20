import json

def reorganize_json(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of dictionaries")

    reorganized_data = {}

    for entry in data:
        country = entry.get("Country", "")
        city = entry.get("City", "")
        year = str(entry.get("Year", ""))

        if country not in reorganized_data:
            reorganized_data[country] = {}

        if city not in reorganized_data[country]:
            reorganized_data[country][city] = {}

        if year not in reorganized_data[country][city]:
            reorganized_data[country][city][year] = {}

        reorganized_data[country][city][year] = {
            key: value for key, value in entry.items() if key not in ["Country", "City", "Year"]
        }

    return reorganized_data

# Specify the paths for your input and output JSON files
input_json_file_path = 'AirQuality.resources.json'
output_json_file_path = 'file_reorganized.json'

# Read the input JSON file
with open(input_json_file_path, 'r') as file:
    input_json = json.load(file)

# Reorganize the JSON
output_json = reorganize_json(input_json)

# Print the reorganized JSON
print(json.dumps(output_json, indent=2))

# Write the reorganized JSON to a new file
with open(output_json_file_path, 'w') as output_file:
    json.dump(output_json, output_file, indent=2)

print(f"Reorganized JSON written to: {output_json_file_path}")




