import sqlite3
import uuid
from validation import Validate_Product


def product_table():
    connect=sqlite3.connect('ecommerce.db')
    cursor= connect.cursor()
    cursor.execute('''
         create table if not exists products(
           product_id text primary key,
           name text not null,
           category text not null,
           price not null,
           stock integer not null
         )  
        
    ''')
    connect.commit()
    connect.close()

init_product_table = product_table

def create_product(name,category,price,stock):
    Validate_Product(name, category, price, stock)
    connect = sqlite3.connect('ecommerce.db')
    cursor = connect.cursor()
    prod_id = str(uuid.uuid4())
    cursor.execute('''
        insert into products (product_id,name,category,price,stock)
        values(?,?,?,?,?)
        ''',(prod_id,name,category,price,stock)

    )
    connect.commit()
    connect.close()

    return {"status":'sucess',
            "product_id":prod_id

    }
