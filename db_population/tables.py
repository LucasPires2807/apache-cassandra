from db_management.create_table import CreateTable

from dotenv import load_dotenv
from os import getenv

load_dotenv()

create_table = CreateTable(getenv('CONTAINER_ID'), 9042, 'store')

schemas = {
    "products": """
        product_id UUID PRIMARY KEY,
        name TEXT,
        description TEXT,
        price DECIMAL,
        stock INT,
        category TEXT,
        created_at TIMESTAMP,
        updated_at TIMESTAMP
    """,
    "customers": """
        customer_id UUID PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        created_at TIMESTAMP,
        updated_at TIMESTAMP
    """,
    "orders": """
        order_id UUID PRIMARY KEY,
        customer_id UUID,
        order_date TIMESTAMP,
        total_amount DECIMAL,
        status TEXT,
        shipping_address TEXT,
        created_at TIMESTAMP,
        updated_at TIMESTAMP
    """,
    "order_items": """
        order_id UUID,
        product_id UUID,
        quantity INT,
        price DECIMAL,
        PRIMARY KEY (order_id, product_id)
    """,
    "categories": """
        category_id UUID PRIMARY KEY,
        category_name TEXT,
        created_at TIMESTAMP,
        updated_at TIMESTAMP
    """,
    "reviews": """
        review_id UUID PRIMARY KEY,
        product_id UUID,
        customer_id UUID,
        rating INT,
        comment TEXT,
        created_at TIMESTAMP
    """
}

for table_name, schema in schemas.items():
    create_table.create_table(table_name, schema)
    print(f"Table '{table_name}' created successfully.")
