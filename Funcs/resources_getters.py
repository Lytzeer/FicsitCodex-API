import json

def get_resources():
    with open("./Data/resources.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return {"resources": data}

if __name__ == "__main__":
    print(get_resources())