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
#print(type(response_txt))
response_txt.to_json

#testing with normalized json
df1 = pd.json_normalize(response_txt)


#removing time from date
df1['releaseDate'] = pd.to_datetime(df1['firstReleaseDate']).dt.date

df3 = df1.drop('firstReleaseDate', axis=1)

#TODO-add new column that assigns a label given the score
#Apparenty this should be done either with numpy or an apply + lambda
#df3['comment'] = 
#if 'topCriticScore' > 95:
#	df3['comment'] = 'Epic'
#elif 'topCriticScore' > 90 AND <95:
#	df3['comment'] = 'Amazing'
###This is the apply function method
# def myfunc(score):
#     if score > 95:
#         myvalue = 'Dope!!!'
#     elif score > 90  and < 95:
#         myvalue = 'Sick'
#     else:
#         myvalue = 'It's ok'
#     return myvalue

# df['new_col'] = df.apply(myfunc, axis=1)


#rearranging columns
#df3 = df3[['name', 'releaseDate', 'topCriticScore', 'tier', 'id', 'images.box.og', 'images.box.sm', 'images.banner.og', 'images.banner.sm']]
df3.sort_values(by=['topCriticScore'], inplace=True, ascending=False)

#creating an index column and naming it 'index'
df3 = df3.reset_index()
df3.rename(columns={'Index': 'index'}, inplace=True)

#exporting to JSON and CSV
df3.to_json('game-list.json', orient='records', indent=2)
df3.to_csv('game-list.csv', index=False)

