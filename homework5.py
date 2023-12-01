from pprint import pprint
from collections import Counter
import os

path_orig = "recipes.txt"
path1 = "1.txt"
path2 = "2.txt"
path3 = "3.txt"

with open(path_orig, encoding='utf-8') as recipes:
    lines = recipes.read().splitlines()

with open(path1, encoding='utf-8') as file_1:
    file1 = file_1.read().splitlines()

with open(path2, encoding='utf-8') as file_2:
    file2 = file_2.read().splitlines()

with open(path3, encoding='utf-8') as file_3:
    file3 = file_3.read().splitlines()

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
    listkeys = []
    for dish in dishes:
        ingridients = task_1()[dish]
        for index,val in enumerate(ingridients):
            val2 = val['ingredient_name']
            listkeys.append(val2)
            count = Counter(listkeys)[val2]
            quantity = val['quantity']
            if val2 in listkeys:
                plus = quantity * count
                multiply = plus * person_count
            else:
                multiply = quantity * person_count
            val.update({'quantity': multiply})
            del val['ingredient_name']
            val_sort_list = (sorted(val.items(), reverse=False))
            val_dict = dict(val_sort_list)
            val3 = {val2: val_dict}
            result.update(val3)
    sort_result = (sorted(result.items(), reverse=False))
    sort_result[4], sort_result[5] = sort_result[5], sort_result[4]
    dict_result = dict(sort_result)
    return dict_result

def task_3(item1, item2, item3):
    f1count = 0
    f2count = 0
    f3count = 0
    dict1 = {}
    dict2 = {}
    dict3 = {}
    main_list = []
    for row in item1:
        f1count = f1count + 1 
    for row in item2:
        f2count = f2count + 1 
    for row in item3:
        f3count = f3count + 1 
    filename1 = os.path.basename(path1)
    filename2 = os.path.basename(path2)
    filename3 = os.path.basename(path3)
    dict1 = {'filename': filename1, 'line_count': f1count, 'line': item1}
    dict2 = {'filename': filename2, 'line_count': f2count, 'line': item2}
    dict3 = {'filename': filename3, 'line_count': f3count, 'line': item3}
    main_list.append(dict1)
    main_list.append(dict2)
    main_list.append(dict3)
    sorted_list = sorted(main_list, key=lambda x: x['line_count'])
    line1 = '\n'.join(sorted_list[0]['line'])
    line2 = '\n'.join(sorted_list[1]['line'])
    line3 = '\n'.join(sorted_list[2]['line'])
    result = (f"{sorted_list[0]['filename']} \n"
    f"{sorted_list[0]['line_count']} \n"
    f"{line1} \n"
    f"{sorted_list[1]['filename']} \n"
    f"{sorted_list[1]['line_count']} \n"
    f"{line2} \n"
    f"{sorted_list[2]['filename']} \n"
    f"{sorted_list[2]['line_count']} \n"
    f"{line3} \n")
    return result   
   
pprint(task_1(), indent=4, sort_dicts=False)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), indent=4, sort_dicts=False)

with open("result.txt", 'w', encoding='utf-8') as result:
        result.write(str(task_3(file1, file2, file3)))