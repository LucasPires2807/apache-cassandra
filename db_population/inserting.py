from db_manipulation.insert import InsertData

from dotenv import load_dotenv
from os import getenv

load_dotenv()

insert_data = InsertData(getenv('CONTAINER_ID'), 9042, 'store', 'products')

# Define the columns for the products table
columns = ['name', 'description', 'price', 'stock', 'category']

# Define a list of product values to be inserted in batch
batch_values = [
    ['Product A', 'Description of Product A', 19.99, 100, 'Category 1'],
    ['Product B', 'Description of Product B', 29.99, 50, 'Category 2'],
    ['Product C', 'Description of Product C', 39.99, 0, 'Category 1'],
    ['Product D', 'Description of Product D', 49.99, 75, 'Category 3'],
    ['Product E', 'Description of Product E', 59.99, 30, 'Category 2'],
]

insert_data.insert_batch_data(columns, batch_values)

