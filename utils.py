import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st 
import os
# from openai import OpenAI 



def format_time_column(df):
    #df['DATETIME'] = pd.to_datetime(df['DATETIME'], format="%H%M")
    
    df = df.sort_values('DATETIME')
    return df 


def plot_base_graph(df,brdf):
    #fig = px.line(df, x="DATETIME", y="BASE_TEMP", markers=True)
    try:
        # Base Temp Fig:
        # fig = go.Figure()

        fig = go.Figure()



        fig.add_trace(go.Scatter(
            x=df['mmdd'],
            y=df['upper_depth_2526'],
            mode='lines+markers',
            name='Upper Depth Bound',
            line=dict(color='yellow'),
            marker=dict(size=4),
            visible='legendonly'
        ))

        fig.add_trace(go.Scatter(
            x=df['mmdd'],
            y=df['mean_depth_2526'],
            mode='lines+markers',
            name='Mean Forecasted Season Depth',
            line=dict(color='royalblue'),
            marker=dict(size=4)

        ))

        fig.add_trace(go.Scatter(
            x=brdf['DATE'],
            y=brdf['BASE_HIN'],
            mode='lines+markers',
            name='Actual Recording',
            line=dict(color='cyan'),
            marker=dict(size=4)

        ))

        fig.add_trace(go.Scatter(
            x=df['mmdd'],
            y=df['lower_depth_2526'],
            mode='lines+markers',
            name='Lower Depth Bound',
            line=dict(color='red'),
            marker=dict(size=4),
            visible='legendonly'
        ))

        fig.update_layout(
            title="2025/2026 Season Progress",
            xaxis_title="Date",
            yaxis_title="Snow Depth (in)",
            template='plotly_dark',
            hovermode='x unified'
        )

        fig.update_layout(
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.5,
                xanchor="center",
                x=0.1
            )
        )



        st.plotly_chart(fig, use_container_width=True)
    except:
        st.error('Could not find weather station data - check BIGROUNDUP')
