import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
np.random.seed(50) ##Gives same values each time

x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x=x_values, y=y_values+5,
                    mode='markers', name='markers')

trace1 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='lines')

trace2 = go.Scatter(x=x_values, y=y_values-5,
                    mode='lines+markers', name='markers+lines')

data = [trace0, trace1, trace2]

layout = go.Layout(title='Line Charts',
                   xaxis=dict(title='X-Axis'),
                   yaxis=dict(title='Y-Axis'))

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='line-graph.html')
