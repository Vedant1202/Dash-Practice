import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/nst-est2017-alldata.csv')

df2 = df[df['DIVISION'] > '0']
df2.dropna(axis=0, inplace=True)
df2.set_index('NAME', inplace=True)

list_population_cols = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_population_cols]
print(df2)

data = [ go.Scatter(x=df2.columns,
                   y=df2.loc[state],
                   mode='lines+markers',
                   name=state) for state in df2.index ]

layout = go.Layout(title='Population statistics for USA states',
                   xaxis=dict(title='X-Axis'),
                   yaxis=dict(title='Y-Axis'))

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Population-line-graph')
