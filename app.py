# Dependencies:
import streamlit as st
import pandas as pd 
from scraper_forecaster import get_live_data
from utils import format_time_column, plot_base_graph, plot_rose_graph, plot_indi1
from plotly.subplots import make_subplots
import os


def main(option='PEAK'):
    # Call the gyro detection:

    # Page UI:
    df = get_live_data()
    df = format_time_column(df)
    
    # Prebuilt Forecasted Season from BigQuery:
    fdf = pd.read_csv('2526f_Streamlit.csv')

    st.title("Snowbird Patrol Dashboard (UNOFFICIAL)")
    st.markdown(f"**Last Updated:** {df['DATETIME'].max()}")
    st.markdown("**Summary of Past 24h:**")
    plot_base_graph(df,fdf)
    #st.write(ai_summary)
            



if __name__ == '__main__':
    main()