import requests
from typing import List
import helpers
from exceptions import APIException

# it does not need to be saved on env file because its shit code and its for abedi's class
api_key = "fxf_KCgGy4oq7JA1yb5OffBg"


headers = {
    "Content-Type": "application/json",
    "apy-token": api_key
}


def send_request(base, to: List[str], amount):
    result = []
    error_message = ""
    error_code = ""
    for i in to:
        api_url = f"https://api.fxfeed.io/v1/convert?api_key={api_key}&from={base}&to={i}&amount={amount}"

        response = requests.get(url=api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            result.append(data["result"])

        else:
            error_message = response.json()["message"]
            error_code    = response.json()["code"]
            raise APIException(error_code=error_code, error_message=error_message)

    
    # helpers.show_error(page, f"{error_code} : {error_message}")

            
    if not error_code or not error_message:
        return result