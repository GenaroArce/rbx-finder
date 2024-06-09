import requests
from bs4 import BeautifulSoup

def convert_nickname_id(nickname):
    url = 'https://users.roblox.com/v1/usernames/users'
    request_body = {
        "usernames": [nickname],
        "excludeBannedUsers": True
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    try:
        response = requests.post(url, json=request_body, headers=headers)
        response.raise_for_status()
        user_data = response.json()
        if user_data['data']:
            return user_data['data'][0]['id']
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

def get_data_id(player_id):
    url = f"https://users.roblox.com/v1/users/{player_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

def get_avatar_user(player_id):
    url = f"https://www.roblox.com/users/{player_id}/profile"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            avatar_url = soup.find('meta', property='og:image')['content']
            if avatar_url:
                return avatar_url
            else:
                return None
        else:
            return None
    except Exception as e:
        return None

def get_data(player_id):
    user_data = get_data_id(player_id)
    if user_data:
        avatar_url = get_avatar_user(player_id)
        if avatar_url:
            user_data["avatar_url"] = avatar_url
        return user_data
    else:
        return None
