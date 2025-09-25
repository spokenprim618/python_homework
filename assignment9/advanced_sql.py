import sqlite3


conn = sqlite3.connect("db\lesson.db")
cursor = conn.cursor()

query = """
SELECT o.order_id, SUM(p.price*i.quantity) AS total_orders
FROM orders AS o
JOIN line_items AS i ON o.order_id = i.order_id
JOIN products AS p ON p.product_id = i.product_id
GROUP BY o.order_id
ORDER BY o.order_id
Limit 5
"""

cursor.execute(query)
results = cursor.fetchall()
print(results)
conn.commit()
conn.close()

conn = sqlite3.connect("db\lesson.db")
cursor = conn.cursor()

query="""
SELECT 
    c.customer_name,
    AVG(orders_sub.total_price) AS average_total_price
FROM customer AS c
LEFT JOIN (
    -- subquery from step 1
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * i.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS i ON o.order_id = i.order_id
    JOIN products AS p ON p.product_id = i.product_id
    GROUP BY o.order_id
) AS orders_sub
ON c.customer_id = orders_sub.customer_id_b
GROUP BY c.customer_id

"""

cursor.execute(query)
results = cursor.fetchall()
print(results)
conn.commit()
conn.close()

conn = sqlite3.connect("db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

cursor.execute("""
    INSERT INTO orders (customer_id, employee_id, order_date)
    VALUES (
        (SELECT customer_id FROM customer WHERE customer_name = 'Perez and Sons'),
        (SELECT employee_id FROM employee WHERE employee_name = 'Miranda Harris'),
        DATE('now')
    )
    RETURNING order_id;
""")
order_id = cursor.fetchall()[0][0]  

cursor.execute(f"""
    INSERT INTO line_items (order_id, product_id, quantity)
    SELECT
        {order_id} AS order_id,
        p.product_id,
        10 AS quantity
    FROM products AS p
    ORDER BY p.price ASC
    LIMIT 5;
""")

cursor.execute(f"""
    SELECT li.line_item_id, li.order_id, li.quantity, p.product_name, p.price
    FROM line_items AS li
    JOIN products AS p ON li.product_id = p.product_id
    WHERE li.order_id = {order_id};
""")
results = cursor.fetchall()
print(results)

conn.commit()
conn.close()
conn = sqlite3.connect("db/lesson.db")
cursor = conn.cursor()

query = """
SELECT e.employee_id,
        e.first_name,
        e.last_name,
        COUNT(o.order_id) AS order_count
FROM employees AS e
JOIN orders AS o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5;
"""

cursor.execute(query)
results = cursor.fetchall()
print(results)
conn.commit()
conn.close()