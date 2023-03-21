import requests, json

base_url = " https://www.themealdb.com/api/json/v1/1/search.php?s="

def get_recipe(search):
    
    recibe_url = base_url + search.lower()

    response = requests.get(recibe_url) 
    resp = response.json()

    dict_recipes = {}

    if resp['meals']:
        for recipe in resp['meals']:
            dict_recipes[recipe['strMeal']] = [recipe['strCategory'], recipe['strMealThumb'], recipe['strYoutube']]
        return dict_recipes
    else:
        return False