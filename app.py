#import the appropriate libraries

import streamlit as st
import pandas as pd
import os.path

from PIL import Image

#Add a title and an image

st.write("""Find data on my favorite stocks: Facebook, Tesla, and Microsoft""")

#image = Image.open("/Users/alanniegrant/code_for_days/stockapp.png")
#data_folder = os.path.join("‎⁨Macintosh HD⁩","Users", "macbookprorich", "Documents","code_for_days")
image = Image.open("/Users/alanniegrant/code_for_days/stockapp.png")
st.image(image, use_column_width = True)

#Create a sidebar header

st.sidebar.header('User Input Choices: FB, TSLA, or MSFT')

#Create a function to get the user's input

def get_input():
    start_date = st.sidebar.text_input("Start Date", "1986-03-13")
    end_date = st.sidebar.text_input("End Date", "2021-06-29")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "FB")
    return start_date, end_date, stock_symbol

#Create a function to get the company name

def get_company_name(symbol):
    if symbol == 'FB':
        return 'Facebook'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == 'MSFT':
        return 'Microsoft'
    else:
        'None'

#Create a function to get company data from file

def get_data(symbol, start, end):
    if symbol.upper() == 'FB':
        df = pd.read_csv("/Users/alanniegrant/code_for_days/hist_fb.csv")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("/Users/alanniegrant/code_for_days/hist_tsla.csv")
    elif symbol.upper() == 'MSFT':
        df = pd.read_csv("/Users/alanniegrant/code_for_days/hist_ms.csv")
    else:
        df = pf.DataFrame(columns = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'))
    
    
    #set start and end index rows to 0
    start_row = 0
    end_row = 0
    
    #start the date from the top of the data down
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]) :
            start_row = i
        break

    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 -j
            break

#set index to the date
    df = df.set_index(pd.to_datetime(df['Date'].values))
    return df.iloc[start_row:end_row +1, :]

#Get user's input
start, end, symbol = get_input()

#Get the date range
start = pd.to_datetime(start)
end = pd.to_datetime(end)

#get the data
df = get_data(symbol, start, end)

#company name
company_name = get_company_name(symbol.upper())

#diplay close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])


#diplay volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

st.header('Data Statistics')
st.write(df.describe())
