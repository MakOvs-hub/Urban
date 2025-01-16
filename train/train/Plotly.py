import plotly
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
fig = go.Figure()

#линейный график
x = np.arange(0, 1000, 0.1)
def f(x):
    return x**2
def f2(x):
    return 2*(x**2)

fig = px.scatter(x=x, y=f(x))
fig.show()


#Объединение графиков
fig = px.scatter(x=x, y=f(x))
fig.add_trace(go.Scatter(x=x, y=f2(x)))
fig.show()

# Создание трехмерного графика
z3d = np.linspace(0, 1, 100)
x3d = z3d * np.sin(50 * z3d)
y3d = z3d * np.cos(50 * z3d)

fig3d = go.Figure(data=[go.Scatter3d(
    x=x3d,
    y=y3d,
    z=z3d,
    mode='markers',
    marker=dict(
        size=10,
        color="red",
        colorscale='Viridis',
        opacity=0.7
    )
)])
fig3d.show()

# Создание подвижных графиков

dv = go.Figure(
    data=[go.Scatter(x=[0, 1], y=[0, 2])],
    layout=go.Layout(
        xaxis=dict(range=[0, 7], autorange=False),
        yaxis=dict(range=[0, 7], autorange=False),
        title=dict(text="Начальный заголовок"),
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Начать",
                          method="animate",
                          args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[1, 1], y=[1, 2])]),
            go.Frame(data=[go.Scatter(x=[1, 6], y=[1, 6])]),
            go.Frame(data=[go.Scatter(x=[3, 6], y=[5, 6])],
                     layout=go.Layout(title_text="Конечный заголовок"))]
)
dv.show()

# Создание графика с ползунком
fig = go.Figure()
# Создание графика
for step in np.arange(0, 20, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="GREEN", width=5),
            name="f(x) = " + str(step),
            x=np.arange(0, 20, 0.1),
            y=np.sin(step * np.arange(0, 20, 0.1))))
# Отображение начального положения графика
fig.data[0].visible = True
# Создание ползунка
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Ползунок переключился на шаг: " + str(i)}],
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)
sliders = [dict(
    active=10,
    currentvalue={"prefix": "Частота: "},
    pad={"t": 50},
    steps=steps
)]
fig.update_layout(
    sliders=sliders
)
fig.show()
