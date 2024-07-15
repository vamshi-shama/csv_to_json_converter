import csv
import json

def csv_to_json(csv_file_path, json_file_path, encoding='utf-8'):
    # Read the CSV file
    data = []
    with open(csv_file_path, mode='r', encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    # Write to the JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
csv_file_path = 'Most Streamed Spotify Songs 2024.csv'
json_file_path = 'spotify_data.json'
csv_to_json(csv_file_path, json_file_path, encoding='ISO-8859-1')
