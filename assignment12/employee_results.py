import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

query = """
SELECT 
    last_name, 
    SUM(p.price * l.quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id
ORDER BY revenue DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

conn.close()

df = pd.DataFrame(results, columns=['last_name', 'revenue'])

df.plot(x='last_name', y='revenue', kind='bar', legend=False)
plt.title("Revenue by Employee")
plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
