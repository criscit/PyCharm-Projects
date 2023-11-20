import requests


def translate_file(path, source_lang, target_lang):
    url = "https://api.bard.ai/v2/models/bard/translate/file"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    data = {
        "path": path,
        "source_lang": source_lang,
        "target_lang": target_lang,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"Error: {response.status_code}")


if __name__ == "__main__":
    path = "/path/to/file.txt"
    source_lang = "en"
    target_lang = "es"
    translated_text = translate_file(path, source_lang, target_lang)
    print(translated_text)
