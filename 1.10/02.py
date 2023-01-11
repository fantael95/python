import json
with open('data/moive.json', 'r',encoding='UTF8') as f:
    movie = json.load(f)
    print(movie)

