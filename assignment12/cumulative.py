import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)

df["cumulative_revenue"] = df["total_price"].cumsum()

df.plot(x="order_id", y="cumulative_revenue", kind="line", legend=False)

plt.title("Cumulative Revenue vs Order ID")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")

plt.show()
conn.close()
