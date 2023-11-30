from pprint import pprint


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
        if dish in task_1():
            for ingridient in task_1()[dish]:
                multiply = ingridient['quantity'] * person_count
                ingridient.update({'quantity': multiply})
                result.update(ingridient)
    return (result)


# pprint(task_1(), width=1, sort_dicts=False)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))