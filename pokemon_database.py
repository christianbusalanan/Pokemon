import pandas as pd
import urllib.request
import sqlite3

# Define a user-agent header to mimic a web browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Create a request object with the headers
req = urllib.request.Request('https://pokemondb.net/pokedex/all', headers=headers)

# Open the URL using the request object
with urllib.request.urlopen(req) as response:
    html = response.read()

# Convert to dataframe
data = pd.read_html(html)
df = data[0]

# Save to Database
conn = sqlite3.connect('pokemon.db')
df.to_sql('pokemon', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

print("Data has been successfully stored in 'pokemon.db' database.")
