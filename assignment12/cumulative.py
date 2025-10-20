import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("..\db\lesson.db")
cursor = conn.cursor()

df = pd.DataFrame(conn)

df['cumulative'] = df['total_price'].cumsum()

df.plot(x="cumulative revenue", y="order_id", kind = "line", title=" cumulative revenue vs. order_id")

plt.show()

