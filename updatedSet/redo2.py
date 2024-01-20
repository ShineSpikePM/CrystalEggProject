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
    year = entry.get("Year", None)  # Get the value of "Year" or None if not present

    # Remove "Country", "City", and "Year" from the entry before reorganizing
    entry_without_country_city_year = {key: value for key, value in entry.items() if key not in ["Country", "City", "Year"]}

    # Reorganize the data
    if country not in reorganized_data:
        reorganized_data[country] = {}
    if "City" not in reorganized_data[country]:
        reorganized_data[country]["City"] = {}
    if city not in reorganized_data[country]["City"]:
        reorganized_data[country]["City"][city] = {}

    # Add the "Year" key if it exists
    if year:
        reorganized_data[country]["City"][city]["Year"] = year

    # Add the rest of the entry data
    reorganized_data[country]["City"][city]["Data"] = entry_without_country_city_year

# Write the reorganized data to a new JSON file
with open('reorganized_data.json', 'w') as file:
    json.dump(reorganized_data, file, indent=2)


