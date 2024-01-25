import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen

st.title("Housing Data Explorer")
st.text("LOREM ISPUM...")
    

##MAP

evic_2020_df = pd.read_csv('data/byZIPMonth2020.csv', dtype={"ZIP":str})
evic_2021_df = pd.read_csv('data/byZIPMonth2021.csv', dtype={"ZIP":str})
evic_2022_df = pd.read_csv('data/byZIPMonth2022.csv', dtype={"ZIP":str})
evic_2023_df = pd.read_csv('data/byZIPMonth2023.csv', dtype={"ZIP":str})

with urlopen('https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master'
             '/ri_rhode_island_zip_codes_geo.min.json') as response:
    ri_zips = json.load(response)

months = ["January", "February", "March", "April", "May", "June", "July","August","September","October","November","December"]

month_slider = st.select_slider("Select Month:",options=months)

st.write(month_slider)


curr_map = evic_2020_df
fig2 = go.FigureWidget()
fig2.add_choroplethmapbox(
        geojson=ri_zips,
        locations=curr_map.ZIP,
        featureidkey="properties.ZCTA5CE10",
        z=curr_map[month_slider],
        colorscale="sunsetdark",
        zmin=0,
        zmax=120,
        marker_opacity=0.6,
        marker_line_width=0,
)
fig2.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=8.6,
    mapbox_center={"lat": 41.58, "lon": -71.47},
    width=700,
    height=700,
)
fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig2)




