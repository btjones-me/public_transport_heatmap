
### plot with gmap
import numpy as np
import pandas as pd
import os
import gmplot

# GoogleMapPlotter return Map object
# Pass the center latitude and
# center longitude
gmap1 = gmplot.GoogleMapPlotter(51.5347066, -0.1384114, 10)
gmap1.apikey = os.environ['GOOGLE_DIRECTIONS_KEY']
# Pass the absolute path
path = "plots/map1.html"
gmap1.draw(path)

# import webbrowser
# webbrowser.open(path, new=2)


### plot with plotly and mapbox
import numpy as np
import pandas as pd

upper_left = [51.5350, -0.1939]
lower_right = [51.5232, -0.1569]
lats = np.linspace(upper_left[0], lower_right[0], 10)
lons = np.linspace(upper_left[1], lower_right[1], 10)
coords = [[i, j] for i in lats for j in lons]
coords = np.round(coords, 5)
df = pd.DataFrame(coords, columns=['Latitude', 'Longitude'])
center = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}).median().to_dict()
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', radius=5,
                        center=center, zoom=13,
                        mapbox_style='carto-positron')

tubes = pd.read_csv('C:/Users/benjamin.t.jones/OneDrive - Accenture/Downloads/London stations.csv')
fig = fig.add_densitymapbox(tubes, lat='Latitude', lon='Longitude', radius=5,
                        hover_name="Station", hover_data=["Zone"],
                        center=center, zoom=13)

fig.add_scattergeo(lat=tubes.Latitude, lon=tubes.Longitude)

fig.show()






# from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
# init_notebook_mode()

mapbox_access_token = '...'

data = [
    go.Densitymapbox(lat=df.Latitude, lon=df.Longitude, radius=9, colorscale='Blackbody'),
    go.Densitymapbox(lat=tubes.Latitude, lon=tubes.Longitude, radius=9)
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        style='open-street-map',
        center=center,
        zoom=13
    ),

)

fig = go.Figure(data=data, layout=layout)
fig.show()



def example_multi():
    """https://community.plot.ly/t/take-a-single-df-and-break-it-into-two-scattermapbox-traces-using-list-comprehension/17763/8"""
    from plotly.offline import init_notebook_mode, iplot
    import plotly.graph_objs as go
    init_notebook_mode()

    mapbox_access_token = '...'

    data = [
        go.Scattermapbox(
            lat=['45.5017'],
            lon=['-73.5673'],
            mode='markers',
            marker=dict(
                size=14
            ),
            name='mapbox 1',
            text=['Montreal'],
            subplot='mapbox'
        ),
        go.Scattermapbox(
            lat=['45.7'],
            lon=['-73.7'],
            mode='markers',
            marker=dict(
                size=14
            ),
            name='mapbox 1',
            text=['Montreal 2'],
            subplot='mapbox'
        ),
        go.Scatter(
            y=[1, 3, 2],
            xaxis='x',
            yaxis='y',
            name='scatter 1'
        ),
        go.Scatter(
            y=[3, 2, 1],
            xaxis='x',
            yaxis='y',
            name='scatter 2'
        ),
        go.Bar(
            y=[1, 2, 3],
            xaxis='x2',
            yaxis='y2',
            name='scatter 3'
        ),
        go.Scatter(
            y=[3, 2, 1],
            xaxis='x2',
            yaxis='y2',
            name='scatter 4'
        ),
    ]

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=45,
                lon=-73
            ),
            pitch=0,
            zoom=5,
            domain={
                'x': [0.3, 0.6],
                'y': [0.7, 1.0]
            }
        ),
        xaxis={
            'domain': [0.3, 0.6]
        },
        yaxis={
            'domain': [0.36, 0.6]
        },
        xaxis2={
            'domain': [0.3, 0.6],
            'side': 'bottom',
            'anchor': 'y2'
        },
        yaxis2={
            'domain': [0, 0.3],
            'anchor': 'x2'
        },
        height=700,
        width=700
    )

    fig = go.Figure(data=data, layout=layout)
    iplot(fig)
