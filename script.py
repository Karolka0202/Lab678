import json

def load_json(file_path):
  try:
    with open(file_path, 'r') as file:
      data = json.load(file)
    print("JSON data loaded successfully.")
    return data
  except json.JSONDecodeError as e:
    print("Error decoding JSON: {e}")
  except FileNotFoundError:
    print("File not found.")

if __name__ == "__main__":
  data = load_json('data.json')
  print(data)
