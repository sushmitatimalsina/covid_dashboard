import requests
import pandas as pd

url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df[['country', 'cases', 'deaths', 'recovered']].head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
