from pprint import pprint
import itertools


with open("recipes.txt", encoding='utf-8') as recipes:
    # print(recipes.read())
    lines = recipes.read().splitlines()

def split_list(input_list, separator):
    sublist = []
    for item in input_list:
        if item == separator:
            yield sublist
            sublist = []
        else:
            sublist.append(item)
    yield sublist
    
def transform_data(data):
    dish_name = data[0]
    ingredients = data[2:]
    transformed_ingredients = []

    for ingredient in ingredients:
        ingredient_name, quantity, measure = ingredient.split(' | ')
        transformed_ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': int(quantity),
            'measure': measure
        })

    return {dish_name: transformed_ingredients}

def task_1():
    cook_book = {}
    cook_list = list(split_list(lines, ''))
    for dish in cook_list:  
        cook_book.update(transform_data(dish))
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        ingridients = task_1()[dish]
        for index,val in enumerate(ingridients):
            multiply = val['quantity'] * person_count
            val.update({'quantity': multiply})
            result = result | val
            print(result)


pprint(task_1(), indent=4, sort_dicts=False)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))