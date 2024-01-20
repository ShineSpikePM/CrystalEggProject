import json

# Read the JSON file
with open('AirQuality.resources.json', 'r') as file:
    original_data = json.load(file)

# Initialize an empty dictionary to store the reorganized data
reorganized_data = {}

# Iterate through each entry in the original data
for entry in original_data:
    country = entry["Country"]
    city = entry["City"]
    
    # Remove "Country" and "City" from the entry before reorganizing
    entry_without_country_city = {key: value for key, value in entry.items() if key not in ["Country", "City"]}
    
    # Reorganize the data
    if country not in reorganized_data:
        reorganized_data[country] = {}
    if "City" not in reorganized_data[country]:
        reorganized_data[country]["City"] = {}
    
    reorganized_data[country]["City"][city] = entry_without_country_city
    
    # Move "Year" one key below "City"
    reorganized_data[country]["City"][city]["Year"] = entry["Year"]

# Write the reorganized data to a new JSON file
with open('redo_data.json', 'w') as file:
    json.dump(reorganized_data, file, indent=2)