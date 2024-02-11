import requests
import json
def search_response(question):
    api_url = "https://www.googleapis.com/youtube/v3/search"
    key=""
    with open("api_key.json", "r") as file:
        data = json.load(file)
        key = data['api_key']
    api_key = key
    params = {
        "part": "snippet",
        "q":question,
        "type":"video",
        "key": api_key
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Access the description directly from the response
        with open("youtube.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print("Error:", response.status_code)
        print(response.text)
    return response
