import requests
import json

# Параметры для авторизации
subdomain = 'your_subdomain'  # Поддомен вашего аккаунта на AmoCRM
client_id = 'your_client_id'  # ID клиента
client_secret = 'your_client_secret'  # Секретный ключ
redirect_uri = 'your_redirect_uri'  # URI для редиректа

# Получение кода авторизации (предполагается, что код был получен и сохранен заранее)
auth_code = 'your_auth_code'

# Получение токенов
token_url = f'https://{subdomain}.amocrm.ru/oauth2/access_token'
token_payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri
}
response = requests.post(token_url, json=token_payload)
tokens = response.json()

access_token = tokens['access_token']  # Access token
refresh_token = tokens['refresh_token']  # Refresh token

# Получение списка сделок
deals_url = f'https://{subdomain}.amocrm.ru/api/v4/leads'
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.get(deals_url, headers=headers)
deals = response.json()

# Вывод первой сделки из списка
print(json.dumps(deals['_embedded']['leads'][0], indent=4))
