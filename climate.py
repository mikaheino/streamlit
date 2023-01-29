import streamlit as st
import pandas as pd

data ={'Year':[2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022], 
'Temp':[0.5, -23.8, -6.6, 3.4, -14.9, -3.1, -0.1, -22.7, -3.3, -17.6, -12.3, -4.3, 0.6, -9.4, -1.6, -5.9, -10.9, -9, -22.8, -7.5],
'Snow':[14, 12, 5, 9, 20, 20, 22, 6, 6, 11, 38, 15, 13, 15, 18, 2, 36, 21, 13, 7]
}

chart_data = pd.DataFrame(data)

st.vega_lite_chart(chart_data, 
{
  "title": {
    "text": "Snow amount at Kuusamo, Kiutaköngas (Ruka)",
    "fontSize": "20",
    "color": "85A9C5"
  },
  "width": 600, "height": 400,
  "encoding": {
    "x": {
      "field": "Year"
    },
  },
  
  "layer": [
    {
      "mark": {"opacity": 0.9, "type": "line", "color": "#0047AB"},
      "encoding": {
        "y": {
          "field": "Temp",
          "title": "Temperature (°C)",
          "axis": {"titleColor": "#0047AB"},
          "sort": "descending"
        }
      }
    },
    {
      "mark": {"type": "rect", "tooltip": "Snow amount", "fillOpacity": 0.5},
      "encoding": {
        "y": {
          "field": "Snow",
          "title": "Snow (cm)",
          "axis": {"titleColor":"#85A9C5"},
          "sort": "descending"

        },
        "y2": { 
          "value": 310
        }
      }
    }
  ],

  "resolve": {"scale": {"y": "independent"}}

})
