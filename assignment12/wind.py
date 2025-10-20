import plotly.express as px
import plotly.data as pldata
import pandas as pd
df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))


df['strength'] = df['strength'].str.replace(r'[^0-9.]', '', regex=True)

# Convert to float
df['strength'] = pd.to_numeric(df['strength'], errors='coearce')

fig = px.scatter(df, x='strength', y='frequency',color = 'direction',
                 title=' strength vs. frequency',hover_data=['frequency'])
fig.write_html('wind.html',auto_open=True)