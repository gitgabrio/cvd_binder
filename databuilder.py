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


# Defines the items buyed by a single customer as a 0/1 vector (1 = buyed)
def buy_customer_items():
    items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    buyed_items = sample(range(number_of_items_per_type), number_of_items_per_customer)
    for x in range(number_of_items_per_customer):
        buyed_item = buyed_items[x] 
        items[buyed_item] = 1 
    return items

def buy_customer_items_id(type_indexes, item_indexes, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        type_index = type_indexes[x]
        sub_items_indexes = item_indexes[x]
        str_id = ''
        for y in range(number_of_types):
            for k in range(number_of_items_per_type):
                if y == type_index:
                    str_id += str(sub_items_indexes[k])
                else:
                    str_id += '0'
        items.append(int(str_id))
    return items
    

# Defines the items buyed by all customers
def buy_all_items(type_indexes, created_items, size_of_dataset):
    items = []
    for x in range(size_of_dataset):
        items.append(buy_customer_items())
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
        for y in range(number_of_items_per_type):
            if sub_items_indexes[y] == 1:
                sub_items.append(created_items[type_index][1][y])
        items.append(sub_items)
    return items

   


if __name__ == '__main__':
    created_items = create_items()
    print(created_items)
    
    size_of_dataset=1000
   
    buyed_type_indexes = np.random.randint(0, number_of_types, size_of_dataset)
    buyed_items_indexes = buy_all_items(buyed_type_indexes, created_items, size_of_dataset)
    buyed_customer_items_id = buy_customer_items_id(buyed_type_indexes, buyed_items_indexes, size_of_dataset)
    
    buyed_types = buy_types(buyed_type_indexes, created_items, size_of_dataset)
    buyed_items = buy_items(buyed_type_indexes, buyed_items_indexes, created_items, size_of_dataset)
    
    
    
    raw_data = {'type': buyed_types, 'buyed_items': buyed_items,  'type_index': buyed_type_indexes, 'buyed_customer_items_id': buyed_customer_items_id}
    
    df = pd.DataFrame(raw_data)
    print(df.head())
    
    df.sort_values(by=['type'], ascending=True).to_csv('input_data.csv', index=False)
   # df.to_csv('input_data.csv', index=False)
