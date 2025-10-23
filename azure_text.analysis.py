import requests
import json


subscription_key = "1788mIQ4Uf1P14BBJPefguhvXzxNxxEd3XgQoH2zuhDLlDxV4Dq3JQQJ99BJACYeBjFXJ3w3AAAaACOGpR6h"
endpoint = "https://amaanailanguage.cognitiveservices.azure.com/text/analytics/v3.0/"


headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

body = {
    "documents": [
        {
            "id": "1",
            "language": "en",
            "text": "I had the best day of my life."
        }
    ]
}


def key_phrase_extraction():
    response = requests.post(endpoint + "keyPhrases",
                             headers=headers, json=body)
    if response.status_code == 200:
        result = response.json()
        phrases = result['documents'][0]['keyPhrases']
        print("\nKey Phrases:")
        print(phrases)
    else:
        print(f"Error: {response.status_code} - {response.text}")


def language_detection():
    language_url = endpoint + 'languages'
    response = requests.post(language_url, headers=headers, json=body)
    languages = response.json()
    print("\nLanguage Detection:")
    print(json.dumps(languages, indent=4))


key_phrase_extraction()
language_detection()
