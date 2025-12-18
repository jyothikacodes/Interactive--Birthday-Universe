import requests

def get_legends_from_api(day, month):
    url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/births/{str(month).zfill(2)}/{str(day).zfill(2)}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return [f"{p['text']} ({p['year']})" for p in data.get('births', [])[:5]]
    except:
        return []