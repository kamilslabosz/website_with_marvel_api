import hashlib
import time
import requests

MARVEL_ENDPOINT = "https://gateway.marvel.com/v1/public/"
PUBLIC_API_KEY = 'public_api_key'
PUBLIC_API_KEY_BYTES = b'public_api_key'
PRIVATE_API_KEY = b'private_api_key'


def get_data_from_api(query):
    m = hashlib.md5()
    ts = str(time.time())
    ts_byte = bytes(ts, 'utf-8')
    m.update(ts_byte)
    m.update(PRIVATE_API_KEY)
    m.update(PUBLIC_API_KEY_BYTES)
    hasht = m.hexdigest()

    query_url = MARVEL_ENDPOINT + query + '?ts=' + ts + '&apikey=' + PUBLIC_API_KEY + '&hash=' + hasht
    response = requests.get(url=query_url)

    return response.json()
