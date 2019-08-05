from conection import Conection

conn = Conection()

## Create table and insert data

create_table_string = '''
CREATE TABLE PRODUCTS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ARTICLE_NAME VARCHAR(50) UNIQUE, 
    PRICE INTEGER, 
    SECTION VARCHAR(20)
)'''
insert_data = "INSERT INTO PRODUCTS VALUES('TV',15,'SPORTS')"

#conn.makeQuery(create_table_string)

products_list = [
    ("T-Shirt", 10,"Sports"),
    ("Trousers", 30,"Formal"),
    ("Socks", 2,"Sports")
]
query = "INSERT INTO PRODUCTS VALUES(NULL,?,?,?)"

conn.makeQuery(query,products_list)

## Get values from database

query_select = "SELECT * FROM PRODUCTS"
product_query_list = conn.getList(query_select)
print(product_query_list)

query_object = "SELECT * FROM PRODUCTS WHERE id=1"
result_object = conn.getList(query_object)
value = result_object[0][2]
print(result_object)

## update objects

query_update = f'UPDATE PRODUCTS SET PRICE = {value + 10} WHERE ID = 1'
conn.makeQuery(query_update)
result_object = conn.getList(query_object)
print(result_object)

## delete products

query_delete = 'DELETE FROM PRODUCTS WHERE ID > 3'
conn.makeQuery(query_delete)
product_query_list = conn.getList(query_select)
print(product_query_list)

conn.finish()