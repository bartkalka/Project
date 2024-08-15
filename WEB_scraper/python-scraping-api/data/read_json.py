import json

# Path to the JSON file
file_path = 'output.json'

# Read and print the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))
