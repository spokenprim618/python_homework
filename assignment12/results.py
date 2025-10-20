import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("..\db\lesson.db")
cursor = conn.cursor()

query = """
SELECT last_name, SUM(price * quantity)
AS revenue FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

cursor.execute(query)
results = cursor.fetchall()
print(results)
conn.commit()
conn.close()
df = pd.DataFrame(results)

df.bar(x="employees", y="revenue", title="Revenue vs employees")
plt.show()


