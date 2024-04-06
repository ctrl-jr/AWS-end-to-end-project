import requests
import json
import pandas as pd
import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), 'config/config.conf'))


url = "https://opencritic-api.p.rapidapi.com/game/hall-of-fame"

headers = {
	"X-RapidAPI-Key": parser.get('api_keys', 'rapidapi-key'),
	"X-RapidAPI-Host": parser.get('api_keys', 'rapidapi-host')

}

response = requests.get(url, headers=headers)

#print(response.json())
top_games = json.loads(response.text)
#print("print json_obj:")
#print(json_obj)
game_list = []

for entry in top_games: 
    temp_list = { 
    "game": entry["name"],
    "release-date": entry["firstReleaseDate"],
    "score": entry["topCriticScore"] }

    game_list.append(temp_list) 

 
df = pd.DataFrame(game_list)

#Removing time from date
df['date'] = pd.to_datetime(df['release-date']).dt.date

#Making a new df excluding old release date format
new_df = df[['game', 'date', 'score']]
new_df = new_df.sort_values(by=['score'], ascending=False)

#print(new_df)
#Creating a local CSV to view the list
new_df.to_csv("games.csv", index=False)
print(new_df)