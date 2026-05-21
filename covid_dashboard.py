import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df[['country', 'cases', 'deaths', 'recovered']].head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


clean_df = df[['country', 'cases', 'deaths', 'recovered']]
clean_df = clean_df.rename(columns={
    'country': 'Country',
    'cases': 'Total Cases',
    'deaths': 'Total Deaths',
    'recovered': 'Total Recovered'
})

clean_df= clean_df.sort_values(by='Total Cases', ascending=False).reset_index(drop=True)
print(clean_df.head(1000))

top_10 = clean_df.head(10)

plt.figure(figsize=(10,5))

plt.bar(top_10['Country'], top_10['Total Cases'])

plt.title("Top 10 Countries by COVID Cases")

plt.xlabel("Country")

plt.ylabel("Total Cases")

plt.xticks(rotation=45)

plt.show()
