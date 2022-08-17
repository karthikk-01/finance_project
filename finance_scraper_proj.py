from datetime import date
from sqlite3 import Row
from tokenize import String
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import math

def main():

if __name__ == "__main__":
    main()
# Getting the companies we are scraping for (S&P 500)
def data_retrieval():
    payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    ticker_table = payload[0]
    ticker_table = ticker_table['Symbol']

    for ticker in ticker_table:
        print(f'This ticker is being printed {ticker}')
        requested_data = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=1420156800&period2=1609459200&interval=1d&events=history&includeAdjustedClose=true"
        initial_unclean_data = pd.read_csv(requested_data)
        natural_log_df = pd.DataFrame(columns = ['Date', 'Log Return', 'Normal Return', 'Adj Close'])
        final_df = pd.concat([initial_unclean_data], ignore_index=True)
        for index, row in initial_unclean_data.iterrows():
            date = initial_unclean_data.loc[index]['Date']
            adj_close = initial_unclean_data.loc[index]['Adj Close']
            temp = (row[1:2])
            temp = temp.astype(float)
            temp_30 = initial_unclean_data.iloc[index - 1];
            temp_30_clean = (temp_30[1:2])
            temp_30_clean = temp_30_clean.astype(float)
            nl_val = (temp/temp_30)
            property = "Close"
            nl_val = getattr(nl_val, property)
            normal_val = (temp/temp_30)
            normal_val = getattr(normal_val, property)
            nl_val = math.log(nl_val)
            temp_list = {'Date': date, 'Log Returns': nl_val, 'Normal Return': normal_val, 'Adj Close': adj_close}
            temp_list = pd.DataFrame([temp_list])
            natural_log_df = pd.concat([natural_log_df, temp_list], ignore_index=True)
        
    # Revised Short-Term Mean Reversion
        # Create for loop beginning at x
def short_term_mean_reversion():        
    for index, row in natural_log_df[753:].iterrows():
        date = unclean_df_STMR.loc[index]['Date']
        thirty_day_avg = 0.0;
        natural_log_df.loc[index]['NL Values']
        for i in range(20):
            temp_day_val = natural_log_df.loc[index - 20 + i]['NL Values']
            thirty_day_avg += temp_day_val
        #print(thirty_day_avg)
        temp_list = {'Date': date, 'STMR': thirty_day_avg}
        temp_list = pd.DataFrame([temp_list])    

        # Create a nested for loop that iterates thirty times for previous days, store that value
        # Add to the appropriate date, probably should use loc to match up w the date
        # Create a new column, and append value as a separate data frame

# Revised MOMENTUM
def momentum():
    momentum_column = pd.DataFrame(columns=['momentum'])
    for index, row in natural_log_df[753:].iterrows():
        date = unclean_df_STMR.loc[index]['Date']
        thirty_day_avg = final_df.loc[index - 753]['STMR']
        one_year_avg = 0.0;
        natural_log_df.loc[index]['NL Values']
        for i in range(252):
            temp_day_val = natural_log_df.loc[index - 252 + i]['NL Values']
            one_year_avg += temp_day_val
        momentum_val = one_year_avg/thirty_day_avg
        temp_list = {'momentum': momentum_val}
        temp_list = pd.DataFrame([temp_list])
        momentum_column = pd.concat([momentum_column, temp_list], ignore_index=True)

    # Revised LTMR
def long_term_mean_reversion():
    ltmr_column = pd.DataFrame(columns=['ltmr'])
    for index, row in natural_log_df[753:].iterrows():
        date = unclean_df_STMR.loc[index - 753]['Date']
        one_year_avg = 0.0;
        four_year_avg = 0.0
        natural_log_df.loc[index]['NL Values']
        for i in range(753):
            temp_day_val = natural_log_df.loc[index - 753 + i]['NL Values']
            four_year_avg += temp_day_val
        for i in range(252):
            temp_day_val = natural_log_df.loc[index - 252 + i]['NL Values']
            one_year_avg += temp_day_val
        ltmr_val = four_year_avg/one_year_avg
        temp_list = {'ltmr': ltmr_val}
        temp_list = pd.DataFrame([temp_list])
        ltmr_column = pd.concat([ltmr_column, temp_list], ignore_index=True)

     





