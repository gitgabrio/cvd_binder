from random import random, randrange, getrandbits, randint 
import pandas as pd
import numpy as np
import string

# type_index = item type
# item_index = item object
item_types = ["Book", "Car", "PC"]

def create_item(item_type, item_index):
    return item_type + "-" + str(item_index)

def create_item_names(item_type):
    items = []
    for x in range(10):
        items.append(create_item(item_type, x))
    return items    
            
def create_items():
    items = []
    for x in item_types:
         items.append([x, create_item_names(x)])
    return items          

def buy_item(type_index, item_index):
    return created_items[type_index][item_index]

def buy_items(type_indexes, item_indexes, created_items, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        type_index = type_indexes[x]
        item_index = item_indexes[x]
        item = created_items[type_index][1][item_index]
        items.append(item)
    return items


if __name__ == '__main__':
    created_items = create_items()
    print(created_items)
    
    size_of_dataset=1000
   
    type_indexes = np.random.randint(0, 3, size_of_dataset)
    item_indexes = np.random.randint(0, 9, size_of_dataset)
    
    buyed_items = buy_items(type_indexes, item_indexes, created_items, size_of_dataset)
    
    raw_data = {'type': type_indexes, 'buyed_items': buyed_items}
    
    df = pd.DataFrame(raw_data)
    
    print(df.head())
    df.to_csv('input_data.csv', index=False)
