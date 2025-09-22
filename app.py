# Dependencies:
import streamlit as st
import pandas as pd 
from scraper_forecaster import get_live_data
from utils import format_time_column, plot_base_graph
from plotly.subplots import make_subplots
import os
import json 
from google.cloud import bigquery
from google.oauth2 import service_account


def main(option='PEAK'):
    # Call the gyro detection:

    # Page UI:
    df = get_live_data()
    df = format_time_column(df)
    
    creds_info = json.loads(os.environ['GOOGLE_APP_CREDS'])
    credentials = service_account.Credentials.from_service_account_info(creds_info)
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)


    # Prebuilt Forecasted Season from BigQuery:
    fdf = pd.read_csv('2526f_Streamlit.csv')

    st.title("Snowbird Season Progress Bar")
    st.markdown(f"**Last Updated:** {df['DATETIME'].max()}")
    plot_base_graph(df,fdf)
    #st.write(ai_summary)
    # Print off datasets (test):
    for dataset in client.list_datasets():
        st.write(dataset.dataset_id)        



if __name__ == '__main__':
    main()