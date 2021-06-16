from random import random, randrange, getrandbits, randint, sample 
import pandas as pd
import numpy as np

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


# Defines the items buyed by a single customer
def buy_customer_items(type_index, created_items):
    items = []
    item_indexes = sample(range(10), 6)
    for x in range(6):
        item_index = item_indexes[x]
        item = created_items[type_index][1][item_index]
        items.append(item)
    return items

# Defines the items buyed by all customers
def buy_items(type_indexes, created_items, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        items.append(buy_customer_items(type_indexes[x], created_items))
    return items

# Map the type_index to its name
def buy_types(type_indexes, created_items, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        items.append(created_items[type_indexes[x]][0])
    return items    


if __name__ == '__main__':
    created_items = create_items()
    print(created_items)
    
    size_of_dataset=1000
   
    type_indexes = np.random.randint(0, 3, size_of_dataset)
    
    buyed_items = buy_items(type_indexes, created_items, size_of_dataset)
    buyed_types = buy_types(type_indexes, created_items, size_of_dataset)
    
    
    raw_data = {'type': buyed_types, 'buyed_items': buyed_items}
    
    df = pd.DataFrame(raw_data)
    
    print(df.head())
    df.to_csv('input_data.csv', index=False)
