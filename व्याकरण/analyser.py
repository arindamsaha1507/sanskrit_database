import pandas as pd
import plotly.express as px
from vinyaasa import *

df = pd.read_csv('धातु.csv')

df['दैर्घ्यम्'] = df['धातु'].apply(lambda x: len(get_vinyaasa(x)))

fig = px.bar(df, x='क्रमाङ्क', y='दैर्घ्यम्', color='गण')
fig.show()

fig = px.histogram(df, x='दैर्घ्यम्', color='गण')
fig.show()

# print(df[df['दैर्घ्यम्']==1])