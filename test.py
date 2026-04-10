import requests

url = "https://api.souimagery.fun/v1/chat/completions"
headers = {
    "Authorization": "Bearer sk-Nm3CRnIJjnHgBc8U9lHgN6ZSGU7UXPh3ROLrlPbAvy6N77AS",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-5.4",
    "messages": [{"role": "user", "content": "Explain gravity in one sentence."}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Success!")
    print(response.json()['choices'][0]['message']['content'])
else:
    print(f"Error: {response.status_code}")
    print(response.text)