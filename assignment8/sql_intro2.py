import pandas as pd

import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    sql_statement ="SELECT line_item_id, quantity,product_id, product_name, price FROM line_items JOIN products ON line_items.product_id = products.product_id"
    df = pd.read_sql_query(sql_statement,conn)

print(df.head(5))
df['total']=df['quantity']*df['price']
print(df.head(5))
newGroup = df.groupby('product_name').agg({'line_item_id ':'count','total':'sum','product_name':'first'})
print(newGroup.head(5))

sorted_df = newGroup.sort_values(by='product_name',inplace = False)
sorted_df.reset_index(inplace=True,drop=True)

sorted_df.to_csv('../assignment8/order_summary.csv')