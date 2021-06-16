from random import random, randrange, getrandbits, randint, sample 
import pandas as pd
import numpy as np

# type_index = item type
# item_index = item object
item_types = ["Book", "Car", "PC"]

number_of_items_per_customer = 6
number_of_items_per_type = 10
number_of_types = 3

def create_item(item_type, item_index):
    return item_type + "-" + str(item_index)

def create_item_names(item_type):
    items = []
    for x in range(number_of_items_per_type):
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
    item_indexes = sample(range(number_of_items_per_type), number_of_items_per_customer)
    for x in range(number_of_items_per_customer):
        item_index = item_indexes[x]
        items.append(item_index)
    return items

# Defines the items buyed by all customers
def buy_all_items(type_indexes, created_items, size_of_dataset):
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

# Map the type_index/item_index to its name
def buy_items(type_indexes, item_indexes, created_items, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        type_index = type_indexes[x]
        sub_items = []
        sub_items_indexes = item_indexes[x]
        for y in range(number_of_items_per_customer):
            item_index = sub_items_indexes[y]
            sub_items.append(created_items[type_index][1][item_index])
        items.append(sub_items)
    return items

def buy_items_ids(item_indexes, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        sub_items = ""
        sub_items_indexes = item_indexes[x]
        items_id = 0
        for y in range(number_of_items_per_customer):
            item_index = sub_items_indexes[y]
            sub_items += str(item_index)
        items.append(int(sub_items))
    return items 

# Define the group_id based on type and item buyed
def buy_group(type_index, buyed_items_indexes):
    group_id = type_index * 10
    sub_group_id = 0
    for x in range(number_of_items_per_customer):
        sub_group_id += buyed_items_indexes[x]
    if sub_group_id <= 20:
        return group_id + 1
    elif sub_group_id >= 30:
        return group_id + 3
    else:
        return group_id + 2 
    


if __name__ == '__main__':
    created_items = create_items()
    print(created_items)
    
    size_of_dataset=1000
   
    buyed_type_indexes = np.random.randint(0, number_of_types, size_of_dataset)
    buyed_items_indexes = buy_all_items(buyed_type_indexes, created_items, size_of_dataset)
    buyer_group = list(map(lambda x, y: buy_group(x, y), buyed_type_indexes, buyed_items_indexes))
    
    buyed_types = buy_types(buyed_type_indexes, created_items, size_of_dataset)
    buyed_items = buy_items(buyed_type_indexes, buyed_items_indexes, created_items, size_of_dataset)
    buyed_items_ids = buy_items_ids(buyed_items_indexes, size_of_dataset)
    
    
    raw_data = {'type': buyed_types, 'buyed_items': buyed_items,  'type_index': buyed_type_indexes, 'item_indexes': buyed_items_ids, 'buyer_group': buyer_group}
    
    df = pd.DataFrame(raw_data)
    
    print(df.head())
    df.to_csv('input_data.csv', index=False)
