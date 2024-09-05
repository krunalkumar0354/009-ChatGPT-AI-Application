import os, requests, json

def main(event):

  key = os.getenv("ChatGPT")
  Description = event.get('inputFields').get('content')
  Reason = event.get('inputFields').get('churn_reason')
  preText = "We are losing customer. I will give you description and reason, and want you to summarize it. Here's the Description :- " + str(Description) + ", and here's the reason :- " + str(Reason) + "."
  text = str(Description) + str(Reason)
  openaiURL = "https://api.openai.com/v1/chat/completions"
  headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
  }
  data = {
    "model": "gpt-4",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": f"Summarize this text: {text}"}
    ],
  }
  response = requests.post(openaiURL, headers=headers, data=json.dumps(data))
  if response.status_code == 200:
    summary = response.json()['choices'][0]['message']['content']
  else:
    print("Error:", response.status_code, response.text)
    summary = response.text
    
  return {
    "outputFields": {
      "Description": Description,
      "Reason": Reason,
      "Summary": summary
    }
  }