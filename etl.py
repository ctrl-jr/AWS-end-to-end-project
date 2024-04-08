import requests
import json
import pandas as pd

url = "https://opencritic-api.p.rapidapi.com/game/hall-of-fame"

headers = {
	"X-RapidAPI-Key": "c889eb29f6msh311cbe380da8e68p19e05bjsn1bd591b83fee",
	"X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
response_txt = json.loads(response.text)
print(type(response_txt))

#testing with normalized json
df2 = pd.json_normalize(response_txt)
print('this is df2:')
print(df2)
df2.to_json('game-list.json', orient='records', indent=2)
df2.to_csv('game-list.csv')

#print(response_txt)
game_list = []

# for entry in response_txt: 
#     temp_list = { 
#     "game": entry["name"],
#     "release-date": entry["firstReleaseDate"],
#     "score": entry["topCriticScore"] }

#     game_list.append(temp_list) 

 
# df = pd.DataFrame(game_list)

# #Removing time from date
# df['date'] = pd.to_datetime(df['release-date']).dt.date

# #Making a new df excluding old release date format
# new_df = df[['game', 'date', 'score']]
# new_df = new_df.sort_values(by=['score'], ascending=False)

# #print(new_df)
# #Creating a local CSV to view the list
# new_df.to_csv("games.csv", index=False)
# #print(new_df)