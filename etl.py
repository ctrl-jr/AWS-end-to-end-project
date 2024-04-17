import requests
import json
import pandas as pd

#creating function for adding a new column that assigns a label given the score
def map_score(score):
  if score >= 90:
    return "Masterpiece"
  elif score > 87:
    return "Very Good"
  else:
    return "Solid"




url = "https://opencritic-api.p.rapidapi.com/game/hall-of-fame"

headers = {
	"X-RapidAPI-Key": "c889eb29f6msh311cbe380da8e68p19e05bjsn1bd591b83fee",
	"X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
response_txt = json.loads(response.text)
#print(type(response_txt))

#testing with normalized json
df1 = pd.json_normalize(response_txt)
print("*JSON normalized")

#removing time from date and dropping old date column
df1['releaseDate'] = pd.to_datetime(df1['firstReleaseDate']).dt.date
df2 = df1.drop('firstReleaseDate', axis=1)

#dropping columns we don't need
df2 = df2.drop(columns=['tier', 'id', 'images.box.og', 'images.box.sm', 'images.banner.og', 'images.banner.sm'])
print("**Dropped columns that won't be used")

#creating new column that adds label based on score
df2["tier"] = df2['topCriticScore'].apply(map_score)
print('***New column added')

#creating an index column and naming it 'index'
df2 = df2.reset_index()
df2.rename(columns={'Index': 'index'}, inplace=True)

#read addtional info file (game-list-extra.json)
df_extra = pd.read_json('game-list-extra.json')

#join with 'extra' file and dropping column 'game_index'
df3 = pd.concat([df2,df_extra], axis=1)  
df3 = df3.drop(columns='game_index')
print('****Dataframes merged')

#rearranging columns
df3.sort_values(by=['topCriticScore'], inplace=True, ascending=False)
df3 = df3[['index', 'name', 'topCriticScore', 'tier', 'releaseDate', 'publisher', 'genre']]

#exporting to JSON and CSV
try:
	df3.to_json('game-list.json', orient='records', indent=2)
	df3.to_csv('game-list.csv', index=False)
	print("::::JSON and CSV created!")
    
except Exception as e:
	print(e)
	print("Something went wrong")
