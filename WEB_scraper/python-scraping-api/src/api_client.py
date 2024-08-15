import requests

def get_company_info(api_url, company_name):
    response = requests.get(f'{api_url}?query={company_name}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
