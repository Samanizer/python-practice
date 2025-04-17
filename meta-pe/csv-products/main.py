'''
Given:

Two CSV files:

products.csv: id,name,category

prices.csv: id,price,currency

Tasks:

Join both files by id

Filter by category == electronics

Output: name, price
'''
import csv

def join_and_filter(product_file, price_file):
    prod_data = {}
    with open(product_file) as pf:
        products_reader = csv.DictReader(pf)
        for row in products_reader:
            prod_data[row['id']] = row
    
    price_data = {}
    with open(price_file) as pf:
        price_reader = csv.DictReader(pf)
        for row in price_reader:
            price_data[row['id']] = row
    
    for id in prod_data:
        product = prod_data[id]
        if product['category'] == 'electronics' and id in price_data:
                    print(product['name'], price_data['price'])
    