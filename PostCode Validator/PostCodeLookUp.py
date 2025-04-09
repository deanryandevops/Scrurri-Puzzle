import requests # import requests to get postcode api data

def get_postcode_information(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode}" # calls api for postcode checker

    try:
        response = requests.get(url) # gets response
        response.raise_for_status() # raises status

        data = response.json() # response json stored in data

        if data['status'] == 200: # if response is successful then post code is valid and been found
            print(f"Postcode Found: {postcode}")

    except requests.exceptions.RequestException as e: # error flagged if pattern is valid and cannot be found
        print(f"{postcode}, does not exist")
