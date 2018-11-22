import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(50)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                    size = 15,
                    color = 'rgb(150, 137, 55)',
                    symbol = 'pentagon',
                    line = {'width': 2}
                   ))]

layout = go.Layout(title='First Scatter Plot',
                   xaxis=dict(title='X-Axis'),
                   yaxis=dict(title='Y-Axis'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')
