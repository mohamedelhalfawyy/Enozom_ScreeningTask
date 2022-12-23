import requests


def get_countries():
    # Here we make a get response to get the api data
    response = requests.get("https://countriesnow.space/api/v0.1/countries/population")
    print(f"Status Code: {response.status_code}")

    # we convert the data to json so we can format it
    result = response.json()

    # we get the data section from the retunred api to get the info we want
    data = result['data']

    return data
