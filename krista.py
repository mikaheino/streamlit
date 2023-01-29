import streamlit as st
import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(
    x=["Normal person", "Athlete", "Krista Parmakoski"],
    y=[28, 46, 69],
    mode='markers',
    marker=dict(
        color=[15, 30, 45, 60, 75, 90],
        size=[15, 30, 90],
        showscale=True
        )
)])

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
