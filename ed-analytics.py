import requests
from settings import ACTOR_ID, ACCESS_TOKEN, ANALYTICS_URL

actor_id = ACTOR_ID
access_token = ACCESS_TOKEN
analytics_url = ANALYTICS_URL


def get_analytics_data():
    response = requests.get(analytics_url+actor_id,
                            headers={'Authorization': access_token,
                                     'content-type': 'application/json'})
    if response.status_code == 200:
        response = response.json()
        print (ed_lesson_json)
        return response


if __name__ == "__main__":
    get_request_setup()

